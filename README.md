## What it is?
This is a automatic mac changer
This project is written in python language.
This helps you to change your mac address in every 10 minutes.

## How it works?
It uses root permissions to work.

It generates it own random mac address and then assigns it to
the in tnterface you have assigned.

If you want to change your mac once simply run the changer.py and then stop it 
using below command.
```
Ctrl + c
```
## How to Install
To install this simply follow below commands.
```
git clone https://github.com/T3CHMYTH/mac-changer
cd mac-changer
chmod 777 install.sh
bash install.sh
```
And then
```
chmod 777 Changer.py
```
and then you are all set you can run the mac-canger now.

## How to run?
Before you run the project you need to be aware of the options of the Changeer.py
```
Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        interface name of which mac is to be changed
```
Example: Suppose if I want to change the mac address of wlan0.
>>> There are two methods.

Methond 1
```
python3 Changer.py -i wlan0
```

Methon 2
```
pyhton3 Changer.py --interface wlan0
```
Note-
if you doesn't specify the interface it may return you and error in the program
