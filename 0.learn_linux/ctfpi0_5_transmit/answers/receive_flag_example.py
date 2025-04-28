import time

#
# BEWARE! Race condition might be happening!!
#


answer = []
while True:
	time.sleep(3)
	with open("/app/answers/flag_encoded.txt", "r") as f:
		current = f.read().split()
	if current:
		for el in current:
			answer.append(chr(int(el)))
	print(answer)


