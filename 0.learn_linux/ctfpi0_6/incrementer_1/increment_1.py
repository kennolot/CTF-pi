import time

# clear the file before anything
open("/app/answers/counter.txt", "w").close()

while True:
	# comment this out after part 1
	time.sleep(1)	
        # using volumes, the count gets written into a shared file
	with open("/app/answers/counter.txt", "r+") as f:

		try:
			counter = int(f.read().strip())	
		except:
			counter = 0

		print("Reading from counter.txt:", counter)
		counter += 1
		f.seek(0)
		f.write(str(counter))
		f.truncate()
