# Python Code for a Star Trek Tricorder-like device based on Raspberry Pico or Zero, not sure yet
# Design will be a TR-590 Tricorder

#   Planned Details for device:
# 1.    calendar with date, time and current (negative) stardate (Stardate 0 = 01.01.2323)
# 1.1   World time
# 1.2   Alarm
# 1.3   Countdown
# 2.    Weather station with temperature, humidity and pressure, history of the last 48 hours
# 2.1   Shown values switchable
# 3.    GPS based coordinates with compass                                          (we'll see what we get)
# 4.    Infrared surface temperature scan                                           (he'll do his best)
# 5.    Distance measurement                                                        (not to be 100% reliable)
# 6.    Heartbeat sensor & Blood Oxymeter                                           (not suitable for medical diagnoses!)
# 7.    Laser pointer (also aiming aid for distanceand temperature measurement)     (PewPewPew)
# 8.    Flashlight with Hi-Power-LED (100%, 60%, 30%, SOS at 100%)                  (Haaalp!!)
# 9.    Blinking stuff for demonstration 
# 10.   acoustic feedback                       (optional, will be done if physical space is available) 
# 11.   3.5" LED screen
# 12.   Be surprised!!!                         (maybe a game, tic-tac-toe or something like that)

#       Silent mode: LED notifications only, no sounds (optional, see point 10), sliding button inside the casing
#       On / Off switch with sliding button inside the casing

#   Diagnosis tools:
#       Uptime (show time the device is switched ON)
#       show CPU core temperature
#       show used space and free space on data storage (if additional storage will be implemented)


# Import libraries:
from machine import Pin
from time import time
from time import sleep
#import screen
#from bme280 import bme280

# Describe Pins for LEDs_
PWR = Pin(__.pin.OUT)               # Indicates On/Off, red LED
Torch = Pin(__.pin.OUT)             # 
runLight = Pin(__.pin.OUT)          # Running green lights in front of the device, 8 LEDs in pairs of 2
LedBtnEnvironment = Pin(__.pin.OUT) # LED on button for weather data    - Alpha: Green
LedBtnGPS = Pin(__.pin.OUT)         # LED on button for GPS data        - Beta: Green
LedBtnPointer = Pin(__.pin.OUT)     # LED on button for Laserpointer    - Gamma: Green
LedDistanceScan = Pin(__.pin.OUT)   # LED on Button for distance scan   - Delta: Green
LedBtnTorch = Pin(__.pin.OUT)       # LED on button for torch           - GEO: Yellow
 = Pin(__.pin.OUT)                  #                                   - MET: Yellow
LedBtnOxymeter = Pin(__.pin.OUT)    # LED on button for Pulse-Oxymeter  - BIO: Yellow
LedSwitchUp = Pin(__.pin.OUT)       #                                   - Library UP
LedSwitchDown = Pin(__.pin.OUT)     #                                   - Library DOWN
FrontRed1 = Pin(__.pin.OUT)         #                                   - Front left LED, Red
FrontRed2 = Pin(__.pin.OUT)         #                                   - Front right LED, Red

# Describe Pins for Buttons:
btnTime = (__, Pin.IN, Pin.PULL_DOWN)               # Quick change to Time and Date screen
btnWeather = (__, Pin.IN, Pin.PULL_DOWN)            # Quick change to weather screen
btnGPS = (__, Pin.IN, Pin.PULL_DOWN)                # Quick change to GPS screen
btnDistanceScan = (__, Pin.IN, Pin.PULL_DOWN)       # Quick change to Distance scan
btnPointer = (__, Pin.IN, Pin.PULL_DOWN)            # toggle laserpointer (PewPewPew)
btnTorch = (__, Pin.IN, Pin.PULL_DOWN)              # switch through Torch modes (100%, 60%, 30%, SOS)
reedScreen = (__, Pin.IN, Pin.PULL_DOWN)            # activate screen when device is opened
LibraryUp = (__, Pin.IN, Pin.PULL_DOWN)             # Switch up through modes
LibraryDown = (__, Pin.IN, Pin.PULL_DOWN)           # Switch down through modes

# Describe Pins for sensor modules:
BME = Pin(__, Pin.IN)    # Sensor for humidity, temperature and air pressure
GPS = Pin(__, Pin.IN)    # Sensor for GPS location
Tem = Pin(__, Pin.IN)    # IR-sensor for surface tmeperature
Dis = Pin(__, Pin.IN)    # ToF-sensor for distance scan up to 4 meters
Vita = Pin(__, Pin.IN)   # sensor for heartrate and blood oxygen leves



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











