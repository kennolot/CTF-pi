import random
from string import ascii_lowercase

def generate_3_letter():
	# generate a random 3 letter lowercase password
	password = []
	for i in range(3):		
		password.append(random.choice(ascii_lowercase))
	return "".join(password)

