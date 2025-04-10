# this code is for Pico.
from machine import UART, Pin
import time

# UARTx, baudrate, GPx=RX
uart = UART(0, baudrate=9600, rx=Pin(1))

while True:    
    msg = uart.readline()            
    print("Received:", msg)
    time.sleep(1)

