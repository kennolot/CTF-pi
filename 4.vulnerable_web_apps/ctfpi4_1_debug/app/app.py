### !!!!
### IN THIS SCENARIO THE CODE WOULDN'T BE AVAILABLE
### !!!
### Still it is great to analyze the security flaws.

from flask import Flask
import random

app = Flask(__name__)

# boss said this is a security risk
app.config["DEBUG"] = True  

@app.route("/")
def index():
    numbers = random.sample(range(1, 101), 10)
    return f'''
    <!doctype html>
    <html>
    <head>        
    </head>
    <body>  
        <p>message: DEV message: debug mode active,</p>
        <p>very important sensor reading: {numbers}</p>
    </body>
    </html>
    '''
    


@app.route("/debug")
def debug():
    debug_msg = """* Serving Flask app app.py
        * Environment: development
        * Debug mode: on
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: 123-456-789
        127.0.0.1 - - [05/Feb/2025 10:23:45] GET / HTTP/1.1 200 -
        127.0.0.1 - - [05/Feb/2025 10:23:47] GET /favicon.ico HTTP/1.1" 404 -
    """
    with open("flag.txt", "r") as f:
        flag = f.read().strip()

    return f'''
    <!doctype html>
    <html>
    <head>
    </head>
    <body>  
        <p>debug_mode: True</p>
        <p>debug_msg: {debug_msg}</p>
        <p>flag: {flag}</p>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
