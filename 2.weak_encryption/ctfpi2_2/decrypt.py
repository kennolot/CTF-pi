import paho.mqtt.client as mqtt
from Crypto.Cipher import AES
import base64

PORT = 1883
BROKER = "localhost"
TOPIC = "ctfpi"

key = b"my secret key!!!"

# https://www.emqx.com/en/blog/how-to-use-mqtt-in-python



def decrypt_message(encrypted_message):
    

def on_message(client, userdata, msg):
    
