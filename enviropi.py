#!/usr/bin/env python

# Compass in progress, commands involve:
# north = motion.heading(), print(motion.heading()), 
# corr_heading = (motion.heading() - north) % 360
# Referenced @ 
# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat

import time
from envirophat import light, motion, weather, leds

print("""Light the LEDs upon temperature increase.

Press Ctrl+C to exit.

""")

threshold = None

try:
    while True:
        north = motion.heading()        
        corr_heading = (motion.heading() - north) % 360
        temperature = weather.temperature()
        fahrenheit = (temperature * 9/5) + 32
        barometric = weather.pressure()
        InHg = (barometric / 3386.39)
        if threshold is None:
            threshold = temperature + 2
        if corr_heading is 345 - 360 or 0 - 15:
            print ("N")
        if corr_heading is 16 - 29:
            print ("NNE")
        if corr_heading is 30 - 60:
            print ("NE")
        if corr_heading is 61 - 74:
            print ("ENE")
        if corr_heading is 75 - 105:
            print ("E")
        if corr_heading is 106 - 119:
            print ("ESE")
        if corr_heading is 120 - 150:
            print ("SE")
        if corr_heading is 151 - 164:
            print ("SSE")
        if corr_heading is 165 - 195:
            print ("S")
        if corr_heading is 196 - 209:
            print ("SSW")
        if corr_heading is 210 - 240:
            print ("SW")
        if corr_heading is 241 - 254:
            print ("WSW")
        if corr_heading is 255 - 285:
            print ("W")
        if corr_heading is 286 - 299:
            print ("WNW")
        if corr_heading is 300 - 330:
            print ("NW")
        if corr_heading is 331 - 344:
            print ("NNW")
            
        print(corr_heading)
        print("{0:.1f} F".format(fahrenheit))
        print("{0:.3f} InHg".format(InHg))
        if temperature > threshold:
            leds.on()
        else:
            leds.off()

        time.sleep(3)

except KeyboardInterrupt:
    pass
