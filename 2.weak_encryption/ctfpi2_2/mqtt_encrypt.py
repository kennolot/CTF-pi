import paho.mqtt.client as mqtt
from Crypto.Cipher import AES
import base64
import os

# https://medium.com/@dheeraj.mickey/how-to-encrypt-and-decrypt-files-in-python-using-aes-a-step-by-step-guide-d0eb6f525e4e

BROKER = "localhost"
TOPIC = "ctfpi"

# encryption part
# i need these two for decrypting my data back!
# not sure if i should keep them here in public though
key = b'my secret key!!!'
iv = b'myinitialvector!'

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # for AES we need 16bytes
    padded_message = message + " " * (16 - len(message) % 16)
    # encode cause we dont want a string, we want bytes
    encrypted_bytes = cipher.encrypt(padded_message.encode())
    # base64 for easier transmission, decode to have text format instead of bytes
    # first 16bytes is IV
    return base64.b64encode(iv + encrypted_bytes).decode()

# mqtt part
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

with open("answers/flag.txt", "r") as f:
    flag = f.read()
encrypted_flag = encrypt_message(flag)

print(f"Encrypted flag published: {encrypted_flag}")
client.publish(TOPIC, encrypted_flag)
client.disconnect()
