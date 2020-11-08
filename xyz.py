import io
import os
import logging
import datetime as dt
from subprocess import Popen, PIPE, DEVNULL
from picamera import PiCamera


DESTINATION = '.'
RESOLUTION = '1280x720'
FRAMERATE = 15 # fps
BITRATE = 1000000 # bps
QUALITY = 22
CHUNK_LENGTH = 300 # seconds
SIZE_LIMIT = 1024 * 1048576 # bytes


class VideoFile:
    def __init__(self, dest=DESTINATION):
        self._filename = os.path.join(
            dest, dt.datetime.utcnow().strftime('CAM-%Y%m%d-%H%M%S.mp4'))
        # Use a VLC sub-process to handle muxing to MP4
        self._process = Popen([
            'cvlc',
            'stream:///dev/stdin',
            '--demux', 'h264',
            '--h264-fps', str(FRAMERATE),
            '--play-and-exit',
            '--sout',
            '#standard{access=file,mux=mp4,dst=%s}' % self._filename,
            ], stdin=PIPE, stdout=DEVNULL, stderr=DEVNULL)
        logging.info('Recording to %s', self._filename)

    def write(self, buf):
        return self._process.stdin.write(buf)

    def close(self):
        self._process.stdin.close()
        self._process.wait()
        # If you want to add a cloud upload, I'd suggest starting it
        # in a background thread here; make sure it keeps an open handle
        # on the output file (self._filename) in case it gets deleted

    @property
    def name(self):
        return self._filename

    @property
    def size(self):
        return os.stat(self._filename).st_size

    def remove(self):
        logging.info('Removing %s', self._filename)
        os.unlink(self._filename)
        self._filename = None


def outputs():
    while True:
        yield VideoFile()


logging.getLogger().setLevel(logging.INFO)
with PiCamera(resolution=RESOLUTION, framerate=FRAMERATE) as camera:
    files = []
    last_output = None
    for output in camera.record_sequence(
            outputs(), format='h264',
            bitrate=BITRATE, quality=QUALITY, intra_period=5 * FRAMERATE):
        if last_output is not None:
            last_output.close()
            files.append(last_output)
            total_size = sum(f.size for f in files)
            while total_size > SIZE_LIMIT:
                f = files.pop(0)
                total_size -= f.size
                f.remove()
        last_output = output
        camera.wait_recording(CHUNK_LENGTH)