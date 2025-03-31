import time
import os.path

internal_counter = 0

while True:
	time.sleep(0.5)
	internal_counter += 1
        # using volumes, the count gets written into a shared file
	with open("/app/answers/counter.txt", "w+") as f:
		print("Counter should be:", internal_counter)
		counter = f.read().strip()
		if not counter.isdigit():
			f.write('0')
		print("We are reading:", counter)

		#f.seek(0)
		counter = int(counter) + 1
		f.write(str(counter))
		#f.truncate()
