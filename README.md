# Envirophat-Pi-US
Pimoroni's EnviroPhat program to display compass, temperature and pressure. Converted to show degrees in Fahrenheit (F) and barometric pressure in Inch of mercury (InHg). 

# What you'll need
Any Raspberry Pi with Raspbian or RaspOS already installed

Pimoroni's Envirophat. In my expereince I used a solderless 40 gpio header and a fan (since I didn't have a heatsink). When it was directly soldered to the board, the pi's heat was causing the temp output to read high.

# Install Envirophat and reboot
sudo apt update && sudo apt full-upgrade -y

curl https://get.pimoroni.com/envirophat | bash

sudo reboot -h now

# Clone the repository 
git clone https://github.com/cy6or9/Envirophat-Pi-US.git

# Enjoy! ;p
cd /Envirophat-Pi-US

python enviropi.py

-- tested on a pi zero w 
