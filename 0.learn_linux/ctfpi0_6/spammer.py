import time

message = '22'

while True:
	time.sleep(0.1)
	with open("answers/flag_encoded.txt", "w") as f:
		f.write(message)

