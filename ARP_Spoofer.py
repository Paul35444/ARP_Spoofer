#!/usr/bin/env python3

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.0.1/24", hwdst="08:00:27:01:af:01", psrc="10.0.1.1") #op=2 creates response instead of request; pdst=IP; hwdst=MAC; psrc=source

