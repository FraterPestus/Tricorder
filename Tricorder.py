# Python Code for Tricorder based on Raspberry Pi Zero

#   Program Details:
# 1.    calendar with date, time and current (negative) sidereal time
# 1.1   World time
# 1.2   Alarm
# 2.    Weather station with temperature, humidity and pressure, history of the last 48 hours
# 2.1   Shown values switchable
# 3.    GPS based coordinates with compass  (we'll see what we get)
# 4.    Surface temperature scan            (he'll do his best)
# 5.    Distance measurement                (not to be 100% reliable)
# 6.    Heartbeat sensor & Blood Oxymeter   (not suitable for medical investigations!)
# 7.    Laser pointer (also as aiming aid for distance measurement) (PewPewPew)
# 8.    Flashlight with Hi-Power-LED (100%, 60%, 30%, SOS at 100%)
# 9.    Blinking stuff for demonstration 
# 10.   acoustic feedback
# 11.   3.5" OLED screen
# 12.   Be surprised!!!

#       Silent mode: LED notification, no sounds

#   Diagnosis tools:
#       Uptime (show time the device is switched ON)
#       show Core temperature
#       show free space on data storage


# Import libraries
from machine import Pin
from time import time
from time import sleep
#from bme280 import bme280

# Describe Pins for LED's
PWR = Pin(__.pin.OUT)
Torch = Pin(__.pin.OUT)


# Describe Pins for Buttons
btnWeather = (__, Pin.IN, Pin.PULL_DOWN)
btnGPS = (__, Pin.IN, Pin.PULL_DOWN)
btnEnvironmentScan = (__, Pin.IN, Pin.PULL_DOWN)
btnDistanceScan = (__, Pin.IN, Pin.PULL_DOWN)
btnPointer = (__, Pin.IN, Pin.PULL_DOWN)
btnTorch = (__, Pin.IN, Pin.PULL_DOWN)
reedScreen = (__, Pin.IN, Pin.PULL_DOWN)


# Describe Pins for sensors
DHT = Pin(__, Pin.IN)
GPS = Pin(__, Pin.IN)
Tem = Pin(__, Pin.IN)
Dis = Pin(__, Pin.IN)
Vita = Pin(__, Pin.IN)


# Create lists for histories
tempHist = ()
humidHist = ()
baroHist = ()



"""
Schleife für Hintergrundscan der Umgebung
while True:
    temp = bme280_temp()
    humid = bme280_humidity()
    baro = bme280_baro()

    TempHist.append(temp)
    if len(tempHist) > 250:
        tempHist.pop()

    humidHist.append(humid)
    if len(humidHist) > 250:
        humidHist.pop()    

    baroHist.append(baro)
    if len(baroHist) > 250:
        baroHist.pop()

"""











