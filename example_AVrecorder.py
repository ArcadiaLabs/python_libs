import time
import datetime
import threading
import subprocess
import os
from camera.AudioRecorder import AudioRecorder
from camera.VideoRecorder import VideoRecorder
from gpiozero import Button
from aiy.pins import BUTTON_GPIO_PIN
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from signal import pause
import math

button = Button(BUTTON_GPIO_PIN)

recording = False

tmp_dir = "/tmp/"
final_dir = "/home/pi/share_nas1/"

def record_ten_seconds():
    file_name = time.time()
    led.on
    start_AVrecording(file_name)
    time.sleep(10)
    stop_AVrecording(file_name)
    led.off
    
def toggle_recording():
    global recording
    global file_name
    if recording == False:
        recording = True
        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        start_AVrecording(file_name)
    else:
        recording = False
        stop_AVrecording(file_name)

def start_AVrecording(file_name):
    print("Starting threads...")
    video_thread.start(file_name, tmp_dir)
    audio_thread.start(file_name, tmp_dir)

def stop_AVrecording(file_name):
    print("Stopping threads...")
    audio_thread.stop()
    video_thread.stop()

    print("starting mux...")
    cmd = "ffmpeg -i {1}/{0}.wav -i {1}/{0}.h264 -c:v copy -c:a aac -strict experimental {2}/{0}.mp4".format(file_name, tmp_dir, final_dir)
    subprocess.call(cmd, shell=True)
    clean_cmd = "rm -rf " + tmp_dir + "/*.wav " + tmp_dir + "/*.h264 "
    subprocess.call(clean_cmd, shell=True)
    print("done")

def main():
    global video_thread
    global audio_thread
    global tmp_dir
    global final_dir

    # Creates tmp directory if does not exist
    tmp_dir = os.path.expanduser(tmp_dir)
    if(os.path.isdir(tmp_dir) == False):
        print("Can't find tmp media directory, creating...")
        os.mkdir(tmp_dir)

    # Creates final media directory if does not exist
    final_dir = os.path.expanduser(final_dir)
    if(os.path.isdir(final_dir) == False):
        print("Can't find media directory, creating...")
        os.mkdir(final_dir)

    # Initializes threads
    video_thread = VideoRecorder(timestamp_fontcolor="white", timestamp_bgcolor="black") 
    # optional params (defaults) : 
        # res_x=640, 
        # res_y=480, 
        # framerate=25, 
        # rotation=0, 
        # timestamp=True, 
        # timestamp_bgcolor="blue", 
        # timestamp_fontcolor="yellow", 
        # timestamp_fontsize=20, 
        # timestamp_format="%d/%m/%Y, %H:%M:%S"
        
    audio_thread = AudioRecorder(device=1) 
    # optional params (defaults) : 
        # device=0, 
        # channels=2, 
        # samplerate=44100

    # Allows time for camera to boot up
    time.sleep(2)
    
        
    # button.when_pressed = record_ten_seconds
    button.when_pressed = toggle_recording
    print("ready for action!")
    
    with Leds() as leds:
        while True:
            if recording:
                leds.update(Leds.rgb_off())
                for i in range(8):
                    leds.update(Leds.rgb_on((2 * i, 0, 0)))
                    time.sleep(0.1)
                for i in reversed(range(8)):
                    leds.update(Leds.rgb_on((2 * i, 0, 0)))
                    time.sleep(0.1)
            else:
                leds.update(Leds.rgb_off())
                for i in range(8):
                    leds.update(Leds.rgb_on((0, 2 * i, 0)))
                    time.sleep(0.1)
                for i in reversed(range(8)):
                    leds.update(Leds.rgb_on((0, 2 * i, 0)))
                    time.sleep(0.1)

if __name__ == "__main__":
    main()