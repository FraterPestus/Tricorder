# Python Code for Tricorder based on Raspberry Pi Zero
# Program Details:
# 1.    Kalender mit Datum, Zeit und aktueller (negativer) Sternzeit
# 1.1   Weltzeit
# 2.    Wetterstation mit Temperatur, Luftfeuchte und -druck, Verlauf der letzten 48 Stunden
# 2.1   Anzuzeigende Werte umschaltbar
# 3.    GPS-basierte Koordinaten mit Kompass
# 4.    Oberflächentemperatur scannen
# 5.    Distanzmessung
# 6.    Laserpointer (auch als Zielhilfe zur Distanzmessung)
# 7.    Taschenlampe mit Hi-Power-LED
# 8.    Blinkezeugs zur Demonstration
# 9.    Akustisches Feedback
# 10.   3,5" OLED-Screen
# 11.   Lasst euch überraschen!!!

# Bibliotheken importieren
from machine import Pin
from time import time
from time import sleep

# LED's definieren
PWR = Pin(0.pin.OUT)
Torch = Pin(0.pin.OUT)


# Taster definieren
btnWetter = ()
btnGPS = ()
btnTempScan = ()
btnDistanceScan = ()
btnPointer = ()
btnTorch = ()
reedScreen = ()


# Sensoren definieren
DHT = Pin(1, Pin.IN)
GPS = Pin()
Tem = Pin()
Dis = Pin()