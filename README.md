# Salesforce-IoT

Salesforce Raspberry Pi

Install Raspbian Headless
1. Download Raspbian Lite Image
2. unzip archive
3. `diskutil list` find device name of SD card, note number #
4. unmount (not eject) card: `diskutil unmountDisk /dev/disk#`
5. copy image `sudo dd bs=1m if=path_of_your_image.img of=/dev/rdisk# conv=sync`
6. wait
7. add SSH file to card
    1. goto card `cd /Volumes/boot`
    2. `touch ssh`
8. eject card
9. Settings -> Sharing -> share Internet through Ethernet
    1. this way Mac has DHCP server giving an IP address to Pi over Ethernet
10. boot Pi
11. find his IP address
    1. `ping raspberrypi.local
    2. or `arp -a` -> IP with [bridge]
12. `ssh pi@IP (192.168.2.2)
    1. password `raspberry`
13. change password
    1. `sudo raspi-config`

Python
suda apt-get update
sudo apt-get install python3-pip

sudo apt-get install python3-dev libffi-dev libssl-dev -y
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
tar xJf Python-3.6.3.tar.xz
cd Python-3.6.3
./configure
make
sudo make install
sudo pip3 install --upgrade pip

sudo chown -R pi /usr/local/lib/python3.7/
sudo rm -r Python-3.7.2

Use Python 3
python3.7
pip3.7

pip3.7 install —user aiosfstream
pip3.7 install —user blinkt
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt

python3.7 IoTcloud/event-receiver.py

Autorun script when online
sudo systemctl edit --force --full iot.service

`
[Unit]
Description=IoT Service
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/IoTcloud
ExecStart=/usr/local/bin/python3.7 /home/pi/IoTcloud/event-receiver.py

[Install]
WantedBy=multi-user.target
`
sudo systemctl enable iot.service
sudo systemctl start iot.service

systemctl status iot.service

Turn off
`sudo poweroff`
sudo systemctl poweroff