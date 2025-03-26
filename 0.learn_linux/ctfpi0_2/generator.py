import random
import string

secret_segments = 10 # for example CTFPI{flag} would be divided ACA, ATA, AFA, APA, AIA, A{A, AfA ...
total_length = 1000 # characters

# read the answer from answers/flag.txt
with open("answers/flag.txt", "r") as flag:
    answer = flag.read().strip()


def generate_secret(index):
    segment = answer[index]

    return fA{segment}A

def generate_random_text(total_length, secret_segments):
    # we don't want 'A' as the random letter since it marks the secret
    letters = string.ascii_uppercase.replace('A', '') + string.ascii_lowercase
    index = 0
    random_text = []

    while True:
        secret_chance = random.randint(0, 100)
        if secret_chance < 5: # 5 % chance to generate the secret at every character.
            segment = generate_secret(index)
            random_text.append(segment)
            index += 1
        else:        
            random_char = random.choice(letters)
            random_text.append(random_char)

random_text = generate_random_text(total_length, secret_segments)

with open("code.txt", "w") as f:
    f.write(random_text)

