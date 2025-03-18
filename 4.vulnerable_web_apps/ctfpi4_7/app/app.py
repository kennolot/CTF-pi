from flask import Flask, request, send_file
import os
import subprocess
app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)


# Credits to: https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
@app.route('/')
def index():    
    
    return f'''    
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
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
    return "Submitted!"

@app.route('/uploads')
def uploads():
    files = os.listdir('uploads')
    files_html = ""
    for file in files:
        files_html += f'<li><a href="/uploads/{file}">{file}</a></li>'
    
    html = f'''
    <!doctype html>
    <html>
    <head>
        <title>Uploaded files</title>
    </head>
    <body>
        <h1>Uploaded files</h1>
        <ul> {files_html} </ul>
        <p><a href="/">Upload more</a></p>
    </body>
    </html>
    '''
    return html


@app.route('/uploads/<filename>')
def download_file(filename):    
    if ".py" in filename and ".." not in filename and "/" not in filename:
        # i wanted to upload my python scripts without relaunching my app
        # i hope its safe                
        output = subprocess.run(['python3', f"uploads/{filename}"], capture_output=True, text=True)
        return f"Python script detected, running: {output}"
    return send_file(f"uploads/{filename}")

app.run(host='0.0.0.0', port=8080, debug=True)
