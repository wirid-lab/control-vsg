#!/usr/bin/env python
#status.py
import os
print("Processing...")
hostname = "192.168.0.2"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print ("Radio Frequency Generator is UP, please continue with the practice!")
else:
    print ("Radio Frecuency Generator is DOWN, please Turn It On!, running the servo.py program")