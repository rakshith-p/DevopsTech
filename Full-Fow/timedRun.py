import time
import os
from Main import *
status = 0
os.system("python *.py")
while True:
	
	if status == 1: 
		time.sleep(60)
	else:
		status = 1
		mainObject = Main()
		time.sleep(60.0)
		status = 0
	
	 #time in seconds to sleep before next run.