#!/usr/bin/env python3

import os

class NetworkStats(object):
    def __init__(self, iface="wlan0"):
        self.iface = iface
    
    def ipv4(self):
        ipv4 = os.popen('ip addr show ' + self.iface).read().split("inet ")[1].split("/")[0]
        return ipv4
        
    def ipv6(self):
        ipv6 = os.popen('ip addr show ' + self.iface).read().split("inet6 ")[1].split("/")[0]
        return ipv6
    
    def essid(self):
        cmd = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}' | sed 's/\"//g'"
        essid = os.popen(cmd).read().rstrip()
        return essid
        
    def rssi(self):       
        cmd = "iwconfig " + self.iface + " | grep Signal | /usr/bin/awk '{print $4}' | /usr/bin/cut -d'=' -f2"
        strDbm = os.popen(cmd).read()
        if (strDbm):
            dbm = int(strDbm)
            quality = 2 * (dbm + 100)
        return quality

if __name__ == "__main__":
    iface = "wlan0"
    wlan0 = NetworkStats(iface=iface)
    
    essid = str(wlan0.essid())
    print(iface + " ESSID : " + essid)
    
    rssi = str(wlan0.rssi())
    print(iface + " signal quality : " + rssi + "%")
    
    ipv4 = str(wlan0.ipv4())
    print(iface + " ipv4 : " + ipv4)
    
    ipv6 = str(wlan0.ipv6())
    print(iface + " ipv6 : " + ipv6)