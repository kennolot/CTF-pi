import time

# reads the flag on this container
with open("./flag.txt", "r") as f:
	flag = f.read().strip()

index = 0
while index < len(flag):
	ascii = ord(flag[index])

	index += 1

	# using volumes, the flag gets written onto a shared file
	with open("./flag_encoded.txt", "a") as f:
	        f.write(str(ascii))

	if index == len(flag):
		index = 0
	time.sleep(5)
