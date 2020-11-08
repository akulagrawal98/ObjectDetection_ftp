import ftplib
session = ftplib.FTP('192.168.1.227','akul',' ')
file = open('img.jpeg','rb')                  # file to send
session.storbinary('STOR Desktop/MP3/Review2/yolo-object-detection/image_akul.jpeg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
