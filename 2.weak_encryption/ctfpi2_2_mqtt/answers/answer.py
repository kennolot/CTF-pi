import paho.mqtt.client as mqtt
from Crypto.Cipher import AES
import base64

PORT = 1883
BROKER = "localhost"
TOPIC = "ctfpi"

key = b"my secret key!!!"

# https://www.emqx.com/en/blog/how-to-use-mqtt-in-python



def decrypt_message(encrypted_message):
    encrypted_data = base64.b64decode(encrypted_message)
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(encrypted_data[16:])
    return decrypted_bytes.decode("utf-8").strip()

def on_message(client, userdata, msg):
    encrypted_msg = msg.payload.decode("utf-8")
    decrypted_msg = decrypt_message(encrypted_msg)
    print(f"Received Encrypted Message: {encrypted_msg}")
    print(f"Decrypted Message: {decrypted_msg}")


client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Listening for messages...")
client.loop_forever()