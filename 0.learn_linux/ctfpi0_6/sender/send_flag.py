import time
import os
import fcntl

spam = '1'

f = open("/app/answers/flag_encoded.txt", "w").close()

while True:
	time.sleep(0.1)
	# using volumes, the character gets written into a shared file
	with open("/app/answers/flag_encoded.txt", "a") as f:
		f.write(spam)
