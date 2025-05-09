from flask import Flask, jsonify, request
import os
import random

app = Flask(__name__)

# boss said this is a security risk
app.config["DEBUG"] = True  

@app.route("/")
def index():
    numbers = random.sample(range(1, 101), 10)
    return jsonify({
        "message": "DEV message: debug mode active",
        "very important sensor reading": numbers
    })


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
        +++ System Ping Enabled +++
        + uses ping command via terminal (os.popen) +
    """
    return jsonify({
        "debug_mode": True,
        "debug_msg": debug_msg
    })

# i introduced this to check if machines in our network can ping eachother.
@app.route("/ping", methods=["GET"])
def ping():
    target = request.args.get("ip", "")
    #       
    response = os.popen(f"ping -c 1 {target}").read()
    print(f"Response: {response}")    
    return f"<pre>{response}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
