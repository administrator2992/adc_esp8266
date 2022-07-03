try:
    import usocket as socket
except:
    import socket

from machine import Pin
from time import sleep
import network
import esp
esp.osdebug(None)

import gc
gc.collect()

#your ssid n password
ssid = 'YourSSID'
password = 'Password'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

def takeip():
    return station.ifconfig()
print(takeip())
