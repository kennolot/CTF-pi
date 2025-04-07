# this code is for raspberry pi
import serial
import time

# /dev/serial part may need changing.
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

with open("answers/flag.txt", "r") as f:
    flag = f.read().strip()

while True:
    ser.write(flag.encode())
    time.sleep(2)
