#!/usr/bin/env python3

from misc import network_infos

iface = "wlan0"
wlan0 = network_infos.NetworkStats(iface=iface)

essid = str(wlan0.essid())
print(iface + " ESSID : " + essid)

rssi = str(wlan0.rssi())
print(iface + " signal quality : " + rssi + "%")

ipv4 = str(wlan0.ipv4())
print(iface + " ipv4 : " + ipv4)

ipv6 = str(wlan0.ipv6())
print(iface + " ipv6 : " + ipv6)