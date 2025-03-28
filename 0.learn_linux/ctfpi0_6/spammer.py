import time

message = '22'
message2 = '333'

while True:
	time.sleep(0.1)
	with open("answers/flag_encoded.txt", "a") as f:
		f.write(message)
	with open("answers/flag_encoded.txt", "a") as f:
                f.write(message2)

