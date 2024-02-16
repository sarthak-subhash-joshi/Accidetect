from flask import Flask,render_template,url_for,request,flash,redirect
from src import utils
from src.pipeline.predict_pipeline import PredictionPipeline
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'accidetect'



@app.route('/')
def home():
    utils.clear_directory('static/results')
    return render_template('index.html')

@app.route('/result',methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        video = request.form.get('video')
        print(video)
        preds_obj = PredictionPipeline()
        result_list=preds_obj.predict(video_path=f'static/uploads/{video}')
        
        print(result_list)
        return render_template('result.html',result_list = result_list)
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5000, debug=True)