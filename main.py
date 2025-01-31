import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "thuocsolai"
AIO_KEY = "aio_yCNv4109DYRmJ8VilgyHGIVmHAbo"

def connected(client):
    print("Ket noi thanh cong ...")
    #client.subscribe(AIO_FEED_ID)
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)
    if feed_id == "button1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "button2":
        if payload == "0":
            writeData("3")
        else :
            writeData("4")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
counter_ai = 5
while True:

    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_detector()
        print("AI Output: ", ai_result)
        client.publish("ai", ai_result)
    readSerial(client)
    time.sleep(1)
    # # Listen to the keyboard for presses.
    # keyboard_input = cv2.waitKey(1)
    #
    # # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
    #     break