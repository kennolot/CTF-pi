# this code is for raspberry pi
import serial
import time

# /dev/ttyAMA0 part may need changing depending on your model, for Pi 5 this works
# on Pi 4 this might be /dev/serial0
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

with open("answers/flag.txt", "r") as f:
    flag = f.read().strip()

while True:
    ser.write(flag.encode())
    print("Sending...")
    time.sleep(2)
