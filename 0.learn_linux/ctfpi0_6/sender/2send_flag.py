import time
import os
import fcntl

spam = '1234567890'

while True:
	time.sleep(0.1)
	# using volumes, the character gets written into a shared file
	with open("/app/answers/flag_encoded.txt", "w") as f:
		fcntl.flock(f, fcntl.LOCK_EX)
		try:
			f.seek(0)
			f.write(spam)
			f.truncate()
			f.flush()
			os.fsync(f.fileno())

		finally:
			fcntl.flock(f, fcntl.LOCK_UN)
