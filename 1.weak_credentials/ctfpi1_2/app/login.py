from flask import Flask, request
from generate_weak_pw import generate_3_letter
import os.path

# load flag
with open(os.path.dirname(__file__) + "../answers/flag.txt", "r") as f:
    flag = f.read().strip()

correct = generate_3_letter()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == correct:
            return flag
        else:
            return "Invalid credentials, please try again."
    return f'''
    <form method="post">
        <p>{correct}</p>
        <label for="password">Password:</label>
        <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    '''

if __name__ == '__main__':
    app.run()
