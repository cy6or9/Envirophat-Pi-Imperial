# Envirophat-Pi-US
Pimoroni's EnviroPhat program to display compass, temperature and pressure. Converted to show degrees in Fahrenheit (F) and barometric pressure in Inch of mercury (InHg). 

# Install Envirophat and reboot
sudo apt update && sudo apt full-upgrade -y

curl https://get.pimoroni.com/envirophat | bash

sudo reboot -h now

# Clone the repository 
git clone https://github.com/cy6or9/Envirophat-Pi-US.git

# Enjoy! ;p
cd /Envirophat-Pi-US

python enviropi.py

