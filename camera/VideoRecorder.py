#!/usr/bin/env python3

import threading
import random
from picamera import PiCamera, Color
import datetime
from time import sleep

class VideoRecorder:
    def __init__(self, res_x=640, res_y=480, framerate=25, rotation=0, timestamp=True, timestamp_bgcolor="blue", timestamp_fontcolor="yellow", timestamp_fontsize=20, timestamp_format="%d/%m/%Y, %H:%M:%S"):
        self.file_name = 'default_name' # This should be replaces with a value given in self.start()
        self.camera = PiCamera()
        self.camera.resolution = (res_x, res_y)
        self.camera.framerate = framerate
        self.camera.rotation = rotation #180
        self.timestamp = timestamp
        self.timestamp_bgcolor = timestamp_bgcolor
        self.timestamp_fontcolor = timestamp_fontcolor
        self.timestamp_fontsize = timestamp_fontsize
        self.timestamp_format = timestamp_format

    def record(self):
        self.camera.start_recording(self.file_name)

        annotate_thread = threading.Thread(target=self.update_annotation)
        annotate_thread.start()

    def stop(self):
        self.camera.stop_recording()

    def update_annotation(self):
        while self.camera.recording:
            if self.timestamp == True:
                self.camera.annotate_background = Color(self.timestamp_bgcolor)
                self.camera.annotate_foreground = Color(self.timestamp_fontcolor)
                self.camera.annotate_text = datetime.datetime.now().strftime(self.timestamp_format)
                self.camera.annotate_text_size = self.timestamp_fontsize
                sleep(1)            

    def start(self, file_name, file_dir):
        self.file_name = '{}/{}.h264'.format(file_dir, file_name)

        video_thread = threading.Thread(target=self.record)
        video_thread.start()