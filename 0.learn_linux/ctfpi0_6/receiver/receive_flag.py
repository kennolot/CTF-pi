import time
import os
import fcntl

while True:
	time.sleep(0.1)
	with open("/app/answers/flag_encoded.txt", "r") as f:
		current = f.read().strip()
		if current == '1':
			print(current)
		else:
			print("Failure detected")

