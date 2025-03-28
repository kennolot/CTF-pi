import time
#
# BEWARE! Race condition might be happening!!
#

spam = '1'

while True:
	time.sleep(0.1)
	# using volumes, the character gets written into a shared file
	with open("/app/answers/flag_encoded.txt", "w") as f:
		f.write(spam)
