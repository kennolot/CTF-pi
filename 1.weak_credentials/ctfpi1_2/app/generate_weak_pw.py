import random
from string import ascii_lowercase

def generate_3_letter():
	# generate a random 3 letter lowercase password
	password = []
	for i in range(1, 3):
		print(i)
		password.append(random.choice(ascii_lowercase))
	return password

