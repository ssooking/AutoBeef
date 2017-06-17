#!/usr/bin/env pthon
#--*--coding=utf-8--*--
# ** Author: ssooking

import json
import urllib2

def getauthkey(host):
    apiurl =  host + "api/admin/login"
    logindata = {
		"username":"beef", 
		"password":"beef"
	}
    jdata = json.dumps(logindata)             # 对数据进行JSON格式化编码
    req = urllib2.Request(apiurl, jdata)      # 生成页面请求的完整数据
    response = urllib2.urlopen(req)           # 发送页面请求
    resdata = response.read()                 # 获取服务器返回的页面信息，数据类型为str
    jsondata =  json.loads(resdata)	      	  # 把数据解析成python对象，此时返回dict数据	  
    return jsondata['token']

if __name__ == '__main__':
	host = "http://192.168.1.133:3000/"
	print getauthkey(host)
