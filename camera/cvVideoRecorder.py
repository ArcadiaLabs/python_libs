#!/usr/bin/env python3

import threading
import random
import cv2
import datetime
from time import sleep

class VideoRecorder:
    def __init__(self, res_x=640, res_y=480, framerate=25, timestamp=True, timestamp_pos=(50,50), timestamp_fontcolor=(255, 255, 255), timestamp_fontsize=1, timestamp_fontthickness=1, timestamp_format="%d/%m/%Y, %H:%M:%S"):
        self.file_name = 'default_name' # This should be replaces with a value given in self.start()
        
        self.camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, res_x)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, res_y)
        self.camera.set(cv2.CAP_PROP_FPS, framerate)
        
        self.framerate = framerate
        self.res_x = res_x
        self.res_y = res_y
        
        
        
        print(self.file_name)
        
        self.timestamp = timestamp
        self.timestamp_pos = timestamp_pos
        self.timestamp_fontcolor = timestamp_fontcolor
        self.timestamp_fontsize = timestamp_fontsize
        self.timestamp_fontthickness = timestamp_fontthickness
        self.timestamp_format = timestamp_format
        
        self.recording = False

    def record(self):
        self.fourcc = cv2.VideoWriter_fourcc('a','v','c','1')
        self.videoWriter = cv2.VideoWriter(self.file_name, self.fourcc, self.framerate, (self.res_x,self.res_y))
        
        self.recording = True
        while self.recording == True:
            ret, frame = self.camera.read()
            if self.timestamp == True:
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                text = datetime.datetime.now().strftime(self.timestamp_format)
                cv2.putText(frame, 
                    text, 
                    self.timestamp_pos, 
                    font, self.timestamp_fontsize, 
                    self.timestamp_fontcolor, 
                    self.timestamp_fontthickness, 
                    cv2.LINE_4)
            self.videoWriter.write(frame)

    def stop(self):
        self.recording = False
        self.camera.release()
        self.videoWriter.release()          

    def start(self, file_name, file_dir):
        self.file_name = '{}/{}.h264'.format(file_dir, file_name)

        video_thread = threading.Thread(target=self.record)
        video_thread.start()