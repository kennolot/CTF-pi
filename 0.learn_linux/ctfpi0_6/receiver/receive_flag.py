import time

#
# BEWARE! Race condition might be happening!!
#

while True:
	time.sleep(0.1)
	with open("/app/answers/flag_encoded.txt", "r") as f:
		current = f.read().strip()
		print(current)

