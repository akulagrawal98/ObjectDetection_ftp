#!/usr/bin/env python3
import ftplib
session = ftplib.FTP('192.168.43.220','akul',' ')
file = open('img.jpeg','rb')                  # file to send
session.storbinary('STOR Document/Semester6/IOT/Innovative/Final_rpi/image_akul.jpeg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

#Conditions
# 1. We should store the images captured in the Home directory
# 2. Images can be copied to the remote location at any place 
