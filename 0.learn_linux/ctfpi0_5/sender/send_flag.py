import time
#
# BEWARE! Race condition might be happening!!
#

# reads the flag on this container
with open("/app/answers/flag.txt", "r") as f:
	flag = f.read().strip()

# clear the flag_encoded.txt
open("/app/answers/flag_encoded.txt", "w").close()

index = 0
while index < len(flag):
	encoded = (ord(flag[index]))
	index += 1

	# using volumes, the flag gets written into a shared file
	with open("/app/answers/flag_encoded.txt", "a") as f:
		f.write(str(encoded) + " ")

	if index == len(flag):
		index = 0 # start the while loop from start when flag.txt end is reached
	time.sleep(3)
