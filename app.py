from flask import Flask,render_template,url_for,request,flash,redirect
from src import utils
from src.pipeline.predict_pipeline import PredictionPipeline
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'accidetect'

# Clear the results folder on first load
utils.clear_directory('static/results')

# Initiate prediction pipeline that includes model loading
preds_obj = PredictionPipeline()


# Routes
@app.route('/')
def home():
    utils.clear_directory('static/results')
    return render_template('index.html')
# Testing route
@app.route('/test')
def test():
    preds_obj.predict('static/uploads/Demo.mp4')
    return "Test Success"
@app.route('/result',methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        video = request.form.get('video')
        print(video)
        result=preds_obj.predict(video_path=f'static/uploads/{video}')
        
        print(result)
        return render_template('result.html',result = result)
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    utils.clear_directory('static/results')