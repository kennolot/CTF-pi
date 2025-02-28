from flask import Flask, request
app = Flask(__name__)

# Credits to: https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask


@app.route('/')
def index():
    return '''    
    <!doctype html>
    <html>
    <head>
        <title>Personal Raspi file hosting server</title>
    </head>
    <body>
        <h1>File Upload</h1>
        <form method="POST" action="" enctype="multipart/form-data">
        <p><input type="file" name="file"></p>
        <p><input type="submit" value="Submit"></p>
        </form>
    </body>
    </html>

    '''
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return "File uploaded!"


app.run()