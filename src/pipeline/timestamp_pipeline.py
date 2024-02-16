import sys
import os
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from tensorflow.keras.models import load_model
import cv2

class AccidentTimestamp:
    def __init__(self):
        pass
    
    def get_timestamp(self,video_path:str,output_array:list):
        try:
            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            logging.info("Loaded the video")
            file_list = []
            current_frame:int = 0
            i:int=0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
        # Extract one frame per second
                if current_frame % int(fps) == 0:
            
                    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                    timestamp_seconds = timestamp / 1000  # Convert to seconds  
                    timestamp_seconds = round(timestamp_seconds,1)
                    timestamp_text = f"{timestamp_seconds}s"
                    output = output_array[i]
                    logging.info("Extracted timestamp")
                    if output == 1:
                        predict="No Accident"
                    else:
                        predict="Accident"
                        flag=1
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame,
                            predict,
                            (50, 50),
                            font, 1,
                            (0, 255, 255),
                            3,
                            cv2.LINE_4)
                    cv2.putText(frame,
                            timestamp_text,
                            (50, 80),
                            font, 1,
                            (0, 255, 255),
                            3,
                            cv2.LINE_4)
                    
                    if output == 0:
                        cv2.imwrite(f"static/results/frame{i}.jpg", frame)
                        file_list.append(f"frame{i}.jpg")

                    i = i+1
        
                current_frame += 1
            cap.release()
            return file_list
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__ == "__main__":
    output_array = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1]
    testing_obj = AccidentTimestamp()
    print(testing_obj.get_timestamp(video_path='artifacts\Demo.mp4',output_array=output_array))
# Testing successful
