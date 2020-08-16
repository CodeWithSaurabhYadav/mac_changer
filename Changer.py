#!/usr/bin/python

#importing modules
import subprocess as sp
import optparse as op
import random
import time
import os
from colored import fg, attr

#colours defining
red = fg(1)
reset = attr("reset")

#parser objects
parser = op.OptionParser()
parser.add_option('-i','--interface',dest='interface',help='interface name of which mac is to be changed')
(options , arguments) = parser.parse_args()
interface = options.interface

#main program i.e. MAC changer
def Changer():
    mac = [ random.randint(0, 255) for x in range(0, 6) ]
    mac[0] = (mac[0] & 0xfc) | 0x02
    mac = ":".join([ '{0:02x}'.format(x) for x in mac ])
    print(mac)
    sp.call(['ifconfig', interface, "down"])
    sp.call('clear')
    sp.call(['ifconfig', interface, 'hw', 'ether', mac])
    sp.call('clear')
    os.system("figlet MAC_CHANGER | lolcat -t -i -p -F -f")
    print (' \t\t----written by saurabh')
    print (f'[+] Changing Mac of {interface} to {mac}')
    time.sleep(2)
    print ('MAC changed sucessfully')
    sp.call(['ifconfig', interface, 'up'])
    print ('New mac will be changed in next 10 mins') 
    print ('Press Ctrl + C to close the mac_chager')

#Checking root privilages
if os.getuid() != 0:
    print ( red + "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting." + reset )
else:
    while 0 < 1 :
            if __name__ == "__main__":
                Changer()
                time.sleep(600)
