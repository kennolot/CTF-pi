import random
import string

# read the answer from answers/flag.txt
with open("answers/flag.txt", "r") as flag:
    answer = flag.read().strip()

secret_segments = len(answer)
total_length = 1000 # characters total

# for example CTFPI{flag} would be divided ACA, ATA, AFA, APA, AIA, A{A, AfA ...

def generate_secret(index, answer):
    segment = answer[index]

    return f"A{segment}A"

def generate_random_text(total_length, secret_segments, answer):
    # we don't want 'A' as the random letter since it marks the secret
    letters = string.ascii_uppercase.replace('A', '') + string.ascii_lowercase
    index = 0
    random_text = []
    pos = 0
    secret_indices = sorted(random.sample(range(total_length), secret_segments))

    while pos < total_length:
        if index < secret_segments and pos == secret_indices[index]:
            random_text.append(generate_secret(index, answer))
            index += 1
        else:
            random_text.append(random.choice(letters))
        pos += 1
    return "".join(random_text)

random_text = generate_random_text(total_length, secret_segments, answer)


with open("code.txt", "w") as f:
    f.write(random_text)

print("Randomly generated secret saved to code.txt")