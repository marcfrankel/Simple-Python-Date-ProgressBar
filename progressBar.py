# (c) Marc Frankel | 2017 | Simple Python Progress Bar for Dates | MIT | V1.2

import time
import sys
import os
import math
from datetime import datetime
os.system('')

def format_time(seconds):
	days = seconds // (60*60*24)
	seconds %= (60*60*24)
	hours = seconds // (60*60)
	seconds %= (60*60)
	minutes = seconds // 60
	seconds %= 60
	return "{:.0f} Days, {:.0f} Hours, {:.0f} Minutes, {:.0f} Seconds".format(days, hours, minutes, seconds)

def create(startDate, endDate):
	totalTime = (endDate - startDate).total_seconds()
	if totalTime < 0:
		return 0 
	now = datetime.now()
	try:
		while now < endDate:
			elasped = (now - startDate).total_seconds()
			sys.stdout.write("Time remaining: {} until {}.\n".format(format_time((endDate - now).total_seconds()), endDate))
			percent = (elasped/(totalTime))*100
			totalWidth = 100
			numberOfLine = math.floor(totalWidth * (percent/100))
			sys.stdout.write("[" + ("\033[92m#\033[0m"* numberOfLine) + (" "* (totalWidth-numberOfLine)) +"] \033[93m {:.6f}% \033[0m\n".format(percent))
			time.sleep(1)
			now = datetime.now()
			if now < endDate:
				sys.stdout.write("\033[F \033[F")
			else: 

				sys.stdout.write("\033[K")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
				sys.stdout.write("\033[K")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
		return 1
	except KeyboardInterrupt:
		sys.stdout.write("\n")
		sys.stdout.write("\n")
		sys.stdout.write("\033[K")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		sys.stdout.write("\033[K")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		return 2
