from machine import Pin, PWM
import ujson
import urequests

while True:
    try:
        for n in range(1, 4001):
            pwm2 = PWM(Pin(2), freq=n, duty=512)
            fjson = {"adc": n}
            jcode = ujson.dumps(fjson).encode()
            #replace your link n apikey
            r = urequests.post("http://<yourip>:<port>/api/adc/<yourapikey>", data=jcode, headers={'Content-Type': 'application/json'})
            r.close()
    except OSError:
        pass
