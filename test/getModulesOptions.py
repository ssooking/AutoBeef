#!/usr/bin/env pthon
#--*--coding=utf-8--*--
# ** Author: ssooking


import requests
import json
import logging

def getModulesOptions(host,modules_id,key):
	r = requests.get("{}/modules/{}?token={}".format(host, modules_id, key)).json()
	print r['options']
	return r['options']

if __name__ == '__main__':
	host = "http://192.168.1.133:3000/api"
	sessionId = "tdipkyoT9fqMsMwrW6oc7esUX74rnuOffhe94T4u2DFRlAjhl5CN47gFikTjccC4YPetBtYhszOqb6MU"
	key = "be531aa684a8fd9ae86c36a3b062697706d9f2d5"
	getoptions(host,169,key)
