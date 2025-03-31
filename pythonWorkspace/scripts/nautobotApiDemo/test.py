#!/bin/python3

import pynautobot

nautobot = pynautobot.api("https://demo.nautobot.com/", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
devices = nautobot.dcim.devices.filter(tenant='Nautobot Baseball Stadiums')

assert len(devices) == 111

if len(devices) != 111:
    raise ValueError
else:
    print("YAY")
