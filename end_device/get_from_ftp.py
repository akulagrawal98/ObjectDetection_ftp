import ftplib

path = 'Desktop'
filename = 'img.jpeg'

ftp = ftplib.FTP("192.168.1.14") 
ftp.login("akul", " ") 
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()
