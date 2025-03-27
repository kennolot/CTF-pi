import time

answer = []
while True:
	time.sleep(7)
	with open("./flag_encoded.txt", "r") as f:
		flag = f.read().strip()
	for el in flag:
		answer.append(chr(el))
		print(answer)


