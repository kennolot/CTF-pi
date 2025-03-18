from flask import Flask, request, send_from_directory
import os
app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)

##
#
# THIS SOURCE CODE REVEALS THE ANSWER AND IS NOT MEANT TO BE VIEWED
# AS PART OF THE CHALLENGE
#
##


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
    <!-- fixed the previous /admin now it should not be so obvious -->
    <!-- i made it hard to guess this time so hackers cant find it!! -->
        <h1>File Upload</h1>
        <form method="POST" action="" enctype="multipart/form-data">
        <p><input type="file" name="file"></p>
        <p><input type="submit" value="Submit"></p>
        </form>
    </body>
    </html>

    '''

@app.route('/whatsnew')
def hidden_uploads():
    with open('flag.txt', 'r') as f:
        read = f.read().strip()
    return read

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
    return send_from_directory('uploads', filename)

app.run(host='0.0.0.0', port=8080, debug=True)
