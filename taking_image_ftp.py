import ftplib
session = ftplib.FTP('192.168.1.227','akul',' ')
#file = open('final_image.py','wb')
session.retrbinary('RETR IMAGE',open('img.jpeg','wb').write)
file.close()
session.quit()
