# Python Code for Tricorder based on Raspberry Pi Zero

#   Program Details:
# 1.    calendar with date, time and current (negative) sidereal time
# 1.1   World time
# 2.    Weather station with temperature, humidity and pressure, history of the last 48 hours
# 2.1   Shown values switchable
# 3.    GPS based coordinates with compass
# 4.    Surface temperature scan
# 5.    Distance measurement
# 6.    Laser pointer (also as aiming aid for distance measurement)
# 7.    Flashlight with Hi-Power-LED (100%, 60%, 30%, SOS at 100%)
# 8.    Blinking stuff for demonstration 
# 9.    acoustic feedback
# 10.   3.5" OLED screen
# 11.   Be surprised!!!

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
DHT = Pin(1, Pin.IN)
GPS = Pin(2, Pin.IN)
Tem = Pin(3, Pin.IN)
Dis = Pin(4, Pin.IN)


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
    humidHist.append(humid)
    baroHist.append(baro)
    if len(tempHist) > 250:
        tempHist.pop()
    if len(humidHist) > 250:
        humidHist.pop()
    if len(baroHist) > 250:
        baroHist.pop()

"""











