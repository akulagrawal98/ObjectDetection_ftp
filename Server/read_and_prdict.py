import os
import subprocess
#file="img.jpeg"
while(True):
	output=subprocess.check_output('find . -name image_akul.jpeg',shell=True)
	#os.system('find . -name img.jpeg')	
	if(output!=b''):
		subprocess.call('python3 yolo.py -i image_akul.jpeg -y yolo-coco',shell=True)
		print("WOW")
#print(type(output))
