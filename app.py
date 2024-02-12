from flask import Flask,render_template,url_for,request,flash,redirect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'accidetect'



@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)