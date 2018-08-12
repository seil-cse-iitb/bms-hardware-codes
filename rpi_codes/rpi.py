'''
init the appliances to the last known state
wait for message
get the message recieved
decode the message
do necessary operation
log the changes to the database
'''
import RPi.GPIO as GPIO
from rpiConfig import appList
from pinConfig import pin_dict
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from rpiConfig import mqttHost,mqttPort,mqttKeepalive,mqttTopicName
import time

from esp_forwarder import send_mqtt_to_esp #moving to esp #added for pawan
#logAction(applianceId,action,forUser,byUser)
#logCurrentStatus(onList,offList):
#getCurrentStatus():

def init():
    GPIO.setmode(GPIO.BOARD)
    time.sleep(1)
    GPIO.setwarnings(False)
    print "Setting up"

    for appliances in pin_dict:
        pin_list = list(pin_dict[appliances])
        for pins in range(0, len(pin_list)):
            GPIO.setup(pin_list[pins],GPIO.OUT)     

    # for i in pinList:
    #    GPIO.setup(pinList[i],GPIO.OUT)
    #    time.sleep(1)

    # onList,offList=getCurrentStatus()
    # for i in onList:
    #     if i !='none':
    #       print i
    #       switchON(pinList[i])
    #       send_mqtt_to_esp(i,1)

    # for i in offList:
    #     if i != 'none':
    #        print i
    #        switchOFF(pinList[i])
    #        send_mqtt_to_esp(i,0)


def on_connect(client, userdata, flags, rc):
    client.subscribe(mqttTopicName,qos=0)
    print "Connected with RC "+ str(rc)


def on_message(client, userdata, msg):
    print msg.payload
    #<name>,<code>, <byuser>
    print(msg.topic)
    
    topic_details = msg.topic.split("/")
    appliance_location = topic_details[-2]
    
    controlAppliance(appliance_location, msg.payload)

def controlAppliance(appliance_location, msg):

    if appliance_location in pin_dict:
        print appliance_location
        pin_list = list(pin_dict[appliance_location])
        print pin_list
        for pins in range(0, len(pin_list)):
            print pin_list[pins]
            if msg[1] == '1':
                GPIO.output(pin_list[pins], True)
            elif msg[1] == '0':
                GPIO.output(pin_list[pins], False)
    else:
        print "Invalide appliance"


if __name__=="__main__":
    init()
    # controlAppliance("F2L", "S1")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqttHost, mqttPort, mqttKeepalive)
    client.loop_forever()
