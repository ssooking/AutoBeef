#!/usr/bin/env pthon
#--*--coding=utf-8--*--
# ** Author: ssooking

import json
import urllib2


def sendConfirm(host, sessionId, authkey):
	postdata = '{}'
	url = host + "api/modules/" + sessionId + "/177?token=" + authkey
	print "[+] URL: " + url
	req = urllib2.Request(url, postdata)
	req.add_header("Content-Type", "application/json; charset=UTF-8")
	f = urllib2.urlopen(req)
	print f.read()

if __name__ == '__main__':
	host = "http://192.168.1.133:3000/"
	sessionId = "tdipkyoT9fqMsMwrW6oc7esUX74rnuOffhe94T4u2DFRlAjhl5CN47gFikTjccC4YPetBtYhszOqb6MU"
	key = "dadd1be063d3a3b4339d84f5bdbbcbb25616b41d"
	sendConfirm(host,sessionId,key)