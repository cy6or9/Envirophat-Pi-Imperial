#!/usr/bin/env python

#Compass in progress, commands involve: north = motion.heading()
#& print(motion.heading()) and the headings 90, 180, 270, 360
#Referenced @ 
#https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat

import time
from envirophat import light, motion, weather, leds

print("""Light the LEDs upon temperature increase.

Press Ctrl+C to exit.

""")

threshold = None

try:
    while True:
        heading = motion.heading()
        temperature = weather.temperature()
        fahrenheit = (temperature * 9/5) + 32
        barometric = weather.pressure()
        InHg = (barometric / 3386.39)
        if threshold is None:
            threshold = temperature + 2
        print("{0:.1f} F".format(fahrenheit))
        print("{0:.3f} InHg".format(InHg))
        if temperature > threshold:
            leds.on()
        else:
            leds.off()

        time.sleep(3)

except KeyboardInterrupt:
    pass
