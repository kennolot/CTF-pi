from flask import Flask, request
import time

app = Flask(__name__)

with open("/tmp/flag.txt", "r") as f:
    flag = f.read().strip()

@app.route("/", methods=["GET"])
def index():
    return "Error 404 Not found"

@app.route("/comunicator", methods=["POST", "GET"])
def comunicator():

    if request.method == "POST":
        guess = request.form.get("password")
    elif request.method == "GET":
        guess = request.args.get("password")
    
    for i in range(len(flag)):  
        try:      
            if guess[i] != flag[i]:
                break
        except:
            break
        # this sleep is the key to simulate side channel attack
        # it acts as if the server is processing the correct input at the background
        # in real side channel attacks these delays wouldn't be so obvious
        time.sleep(0.5)


    if guess == flag:
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Login success</title>
            </head>
            <body>
                <h1>Welcome back, EVILm03</h1>
                <p>Loaded: 23 victim devices so far.</p>
                <h2>{flag}</h2>
            </body>
        </html>
        """
    else:
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Evil attacker server</title>
            </head>
            <body>
                <h1>EVILm03 C2C server</h1>
                <h2>Reminder: i have allowed both POST and GET</h2>
                <p>to access the victim devices i have to sign in first</p>
                <p><b> POST form data is "password" and GET query param is also "password" </b></p>
                <p>{guess}</p>
            </body>
        </html>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
