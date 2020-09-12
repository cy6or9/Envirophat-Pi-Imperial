# Envirophat-Pi-Imperial
Pimoroni's EnviroPhat converted to show degees in fahrenheit (F) and barmetric pressure in Inch of mercury (InHg).

# Install Envirophat and reboot
sudo apt update && sudo apt full-upgrade -y

curl https://get.pimoroni.com/envirophat | bash

sudo reboot -h now

# Clone the repository 
git clone git@github.com:cy6or9/Envirophat-Pi-Imperial.git

# Enjoy! ;p
cd /Envirophat-Pi-Imperial

python enviropi.py

