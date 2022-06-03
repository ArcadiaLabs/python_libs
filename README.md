# Python Libraries
A lot of these libraries find a use with developer boards (Raspberry Pi, BBB...)

For additional details about a specific function, see the lib file header.

###      Camera
#### camera
For use with pygame, functions to use a usb webcam
#### VideoRecorder / AudioRecorder
Records audio + video using picamera and ffmpeg. Requires picamera, pyaudio, wave, gpiozero (see *example_AVrecorder.py* for usage)
#### cvVideoRecorder / AudioRecorder
Records audio + video using OpenCV and ffmpeg. Requires OpenCV, pyaudio, wave, gpiozero (see *example_cvAVrecorder.py* for usage)

###      Draw 
##### drawfunctions
For use with pygame, allows better placement of texts and pictures and allows text outline. 

###      I2C
##### i2c_core
I2C core functions, needed by other i2c libs. Should autodetect Raspberry and Banana boards i2c bus number.
#### i2c_at24cxx
ATMEL AT24C16 16kb I2C EEPROM and AT24CXX series *(not sure how to correctly use these EEPROM chips)*
#### i2c_bmp085
Bosch BMP085 pressure and temperature sensor 
#### i2c_ds1621
Maxim DS1621 I2C Temperature sensor, Low accuracy (0.5°C)
#### i2c_ds1624
Maxim DS1624 I2C Temperature sensor + 256b eeprom, High accuracy (0.03°C)
#### i2c_hmc5883l
Honeywell HMC5883L Magnetometer
#### i2c_lcd2004
HD44780 / LCD2004 20x4 characters LCD
#### i2c_pca9685
NXP PCA9685 16 Channels PMW controller

###      Misc
##### network_infos
Shows ipv4, ipv6, ESSID and RSSI for a network interface. See *example_networkInfos.py* for usage.
#### socket_gps
Connects to an open socket, and grabs position data. Usually works with an android device server and a custom apk.
#### xbox_read 
Reads inputs from a xbox360 wireless controller and sends as events to the system *(must check if still works)*
#### colors
Colors helpers in BGR format.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?business=W8GSHCVF6N748&no_recurring=0&currency_code=EUR)
