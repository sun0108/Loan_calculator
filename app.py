from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html',pageTitle='Calculator main page')

if __name__ == '__main__':   
     app.run(debug=True, host='0.0.0.0')