from flask import Flask, request
from generate_weak_pw import generate_3_letter

# load flag
with open("flag.txt", "r") as f:
    flag = f.read().strip()

correct = generate_3_letter()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():    
    if request.method == "POST":
        password = request.form['password']
        if password == correct:
            return flag
        else:
            return "Invalid credentials, please try again."
    return '''
    <form method="post">           
        <label for="password">Password:</label>
        <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
