# this code is for Pico.
from machine import UART, Pin
import time

# UARTx, baudrate, GPx=TX, GPx=RX
uart = UART(0, baudrate=9600, tx=Pin(17))

while True:
    if uart.any():
        msg = uart.readline()
        if msg:
            decoded = msg.decode('utf-8').strip()
            print("Received:", decoded)
    time.sleep(1)
