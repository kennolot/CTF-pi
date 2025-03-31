import time
import os
import fcntl

while True:
	time.sleep(0.1)
	with open("/app/answers/flag_encoded.txt", "r") as f:
		fcntl.flock(f, fcntl.LOCK_SH)
		try:
			current = f.read().strip()
			print(current)
		finally:
			fcntl.flock(f, fcntl.LOCK_UN)

