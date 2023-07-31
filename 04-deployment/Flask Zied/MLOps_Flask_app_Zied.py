from flask import Flask , render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

@app.route('/', methods = ['GET'])
def hello():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the audio file from post request
        f = request.files['t1']
        # Save the audio file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

    return file_path

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9696)