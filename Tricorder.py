# Python Code for a Star Trek Tricorder-like device based on Raspberry Pico or Zero, not sure yet
# Design will be a TR-590 Tricorder

#   Planned Details for device:
# 1.    calendar with date, time and current (negative) stardate (Stardate 0 = 01.01.2323)
# 1.1   World time
# 1.2   Alarm
# 2.    Weather station with temperature, humidity and pressure, history of the last 48 hours
# 2.1   Shown values switchable
# 3.    GPS based coordinates with compass      (we'll see what we get)
# 4.    Infrared surface temperature scan       (he'll do his best)
# 5.    Distance measurement                    (not to be 100% reliable)
# 6.    Heartbeat sensor & Blood Oxymeter       (not suitable for medical diagnoses!)
# 7.    Laser pointer (also as aiming aid for distance measurement)     (PewPewPew)
# 8.    Flashlight with Hi-Power-LED (100%, 60%, 30%, SOS at 100%)      (Haaalp!!)
# 9.    Blinking stuff for demonstration 
# 10.   acoustic feedback                       (optional, will be done if physical space is available) 
# 11.   3.5" LED screen
# 12.   Be surprised!!!                         (maybe a game, tic-tac-toe or something like that)

#       Silent mode: LED notification, no sounds (optional, see point 10)

#   Diagnosis tools:
#       Uptime (show time the device is switched ON)
#       show CPU core temperature
#       show free space on data storage (if additionla storage will be implemented)


# Import libraries
from machine import Pin
from time import time
from time import sleep
#from bme280 import bme280

# Describe Pins for LED's
PWR = Pin(__.pin.OUT)               # Indicates On/Off, red LED
Torch = Pin(__.pin.OUT)             # 
runLight = Pin(__.pin.OUT)          # Running lights in front of the device, 8 LEDs in pairs of 2
LedBtnEnvironment = Pin(__.pin.OUT) # LED on button for weather data, yellow LED
LedBtnGPS = Pin(__.pin.OUT)         # LED on button for GPS data, yellow LED
LedBtnPointer = Pin(__.pin.OUT)     # LED on button for Laserpointer, yellow LED
LedDistanceScan = Pin(__.pin.OUT)   # LED on Button for distance scan, yellow LED
LedBtnTorch = Pin(__.pin.OUT)       # LED on button for torch, yellow LED
 = Pin(__.pin.OUT)

# Describe Pins for Buttons
btnWeather = (__, Pin.IN, Pin.PULL_DOWN)
btnGPS = (__, Pin.IN, Pin.PULL_DOWN)
btnEnvironmentScan = (__, Pin.IN, Pin.PULL_DOWN)
btnDistanceScan = (__, Pin.IN, Pin.PULL_DOWN)
btnPointer = (__, Pin.IN, Pin.PULL_DOWN)
btnTorch = (__, Pin.IN, Pin.PULL_DOWN)
reedScreen = (__, Pin.IN, Pin.PULL_DOWN)


# Describe Pins for sensors
BME = Pin(__, Pin.IN)
GPS = Pin(__, Pin.IN)
Tem = Pin(__, Pin.IN)
Dis = Pin(__, Pin.IN)
Vita = Pin(__, Pin.IN)


# Create lists for histories
tempHist = ()
humidHist = ()
baroHist = ()


# Here the fun starts:

"""
Loop for permanent background environment scan
while True:
    temp = bme280_temp()
    humid = bme280_humidity()
    baro = bme280_baro()

    TempHist.append(temp)
    if len(tempHist) > 289:
        tempHist.pop()

    humidHist.append(humid)
    if len(humidHist) > 289:
        humidHist.pop()    

    baroHist.append(baro)
    if len(baroHist) > 289:
        baroHist.pop()

"""











