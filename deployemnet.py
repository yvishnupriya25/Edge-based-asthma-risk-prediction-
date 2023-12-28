import tensorflow
import RPi.GPIO as GPIO
import numpy as np
import paho.mqtt.client as mqtt
import requests
import time
import sklearn
import asthama
MQTT_SERVER = "broker.hivemq.com"
MQTT_TOPIC = "home/livingroom"
actual_pefr=350
redled=23
greenled=26
yellowled=24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    print("Connected to MQTT server with result code " + str(rc))

def on_message(client, userdata, msg):
    c=0
    print(msg)
    payload=msg.payload.decode("utf-8")
    print(payload)
    x=payload.split(',')
    data=[]
    for i in x:
        if(i=='Test data for testing'):
            continue
        else:
            c=c+1
            a=float(i)
            if(c%4==1):
                data=[]
                data.append(a)
            else:
                
                data.append(a)
                
                age=52
                height=125
                gender=1
                if len(data)==4:
                    h=data[0]
                    t=data[1]
                    pm25=data[2]
                    pm10=data[3]
                    print("hum:",h)
                    print("temp:",t)
                    print("pm2.5:",pm25)
                    print("pm10:",pm10)
                
                
                #The normal peak flow is 450-550 L /min in adult males and it is 320-470 L/min in adult females
                    params = np.array([age, height, gender, t, h, pm25, pm10])
                    params=params.reshape(1,7,1)
                    predicted_pefr=asthama.model.predict(params)
                    predicted_pefr=predicted_pefr+300
                    print("predicted pefr:",predicted_pefr)
                    perpefr=(actual_pefr/predicted_pefr)*100
                    if perpefr>=80:
                        print("safe")
                        GPIO.output(26,GPIO.HIGH)
                    elif perpefr>=50:
                        print("moderate")
                        GPIO.output(24,GPIO.HIGH)
                    else:
                        print("risk")
                        GPIO.output(23,GPIO.HIGH)
                    
                    
                    
            
            
            
            
            
            
        
            
            
           
  
   
   
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()
