import sys
import os
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from tensorflow.keras.models import load_model
import cv2

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,video_path):
        try:
            model_path = 'artifacts\model.h5'
            logging.info("loaded the model")
            model = load_model(model_path)
            cap = cv2.VideoCapture(video_path)
            logging.info("Loaded the video")
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            current_frame = 0
            i=0
            output_vector = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                # Extract one frame per second
                if current_frame % int(fps) == 0:
                    frame = cv2.resize(frame,(224,224))
                    frame  = np.expand_dims(frame,axis=0)
                    frame = frame/255.0
                    output = model.predict(frame)
                    if output < 0.5:
                        output=0
                    else:
                        output = 1
                    output_vector.append(output)

                    i = i+1
                current_frame += 1
            cap.release()
            logging.info("Prediction Done and outputs saved")
            return output_vector
        except Exception as e:
            raise CustomException(e,sys)
        




# if __name__ == "__main__":
#     prediction_obj = PredictionPipeline()
#     print(prediction_obj.predict('artifacts\Demo.mp4'))
# 
    