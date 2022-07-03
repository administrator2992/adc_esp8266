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

  ![image](https://user-images.githubusercontent.com/57089541/177039989-a64d9472-87dd-4c41-85f7-6777cece2880.png)

Generate READ API Key dan WRITE API Key

  ![image](https://user-images.githubusercontent.com/57089541/177039765-cbbe352b-b345-42fb-89b5-859c4689475d.png)

## Installation for ESP8266

If you not ready for micropython, watch this youtube video : 

[![SC2 Video](https://img.youtube.com/vi/CPkzcNIVqPQ/0.jpg)](https://youtu.be/CPkzcNIVqPQ)

If micropython is ready, copy code in [boot.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/boot.py) and [main.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/main.py) in [micropython-esp8266_code](https://github.com/administrator2992/adc_esp8266/tree/dev/micropython-esp8266_code) folder and paste [boot.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/boot.py) code to file boot.py from ESP8266 and paste [main.py](https://github.com/administrator2992/adc_esp8266/blob/dev/micropython-esp8266_code/main.py) code to file main.py from ESP8266. Change your SSID and password in boot.py and change your IP Server, Port, and Your WRITE API Key in main.py

#### Run Program with Thonny
Choose stop/restart backend (red botton in text "STOP")

  ![image](https://user-images.githubusercontent.com/57089541/177040003-0c6c41e6-626e-4904-94b4-0510591a6b45.png)

If LED in ESP8266 is Blinking faster, your network is correct, if not yet, LED blinking is not to be faster

## DEMO

#### Access IP server following /api/adc/'your-readapikey' for view data uploaded from ESP8266

Ask the issue/bug this program in Issues Menu : https://github.com/administrator2992/adc_esp8266/issues

Thanks (❁´◡`❁)
