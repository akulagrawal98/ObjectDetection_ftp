import ftplib
path = 'Desktop/MP3/Review2/yolo-object-detection'
filename = 'image_class.jpeg'
ftp = ftplib.FTP("192.168.1.14") 
ftp.login("akul", " ") 
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()
