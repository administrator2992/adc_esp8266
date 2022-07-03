# Fake ADC ESP8266 API

## How This System Program Works

  ![image](https://github.com/administrator2992/adc_esp8266/blob/dev/flowchart.png)

## Installation for Server

First, create python environtment

#### For CMD
```cmd
  python -m venv adc_esp
  adc_esp\Scripts\activate
```
#### For Terminal
```cmd
  python -m venv adc_esp
  source adc_esp/bin/activate
```

Open terminal and install package by [requirements.txt](https://github.com/administrator2992/adc_esp8266/blob/dev/requirements.txt)

```bash
  pip install -r requirements.txt
```
Run [main.py](https://github.com/administrator2992/adc_esp8266/blob/dev/main.py)

```bash
  python main.py
```

Access Your localhost/IP Server. You can get IP server in your terminal/CMD

  ![Screenshot](https://github.com/administrator2992/adc_esp8266/blob/dev/main.jpg)

## Installation for ESP8266

If you not ready for micropython, watch this youtube video : 

[![SC2 Video](https://img.youtube.com/vi/CPkzcNIVqPQ/0.jpg)](https://youtu.be/CPkzcNIVqPQ)

If micropython is ready, copy code in [boot.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/boot.py) and [main.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/main.py) in [micropython-esp8266_code](https://github.com/administrator2992/adc_esp8266/tree/dev/micropython-esp8266_code) folder and paste [boot.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/boot.py) code in file boot.py from ESP8266 and paste [main.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/main.py) code in file main.py from ESP8266. Change your SSID and password in boot.py and change your IP Server, Port, and Your WRITE API Key in main.py

#### Run Program with Thonny
Choose start/restart backend (red botton in text "STOP")

  ![Screenshot](https://github.com/administrator2992/adc_esp8266/blob/dev/play.jpg)

If LED in ESP8266 is Blinking faster, your network is correct, if not yet, LED blinking is not to be faster

Ask the issue/bug this program in Issues Menu : https://github.com/administrator2992/adc_esp8266/issues

Thanks (❁´◡`❁)
