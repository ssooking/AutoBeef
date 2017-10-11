### a simple demo to autorun beef modules

See the blog http://www.cnblogs.com/ssooking/p/6959239.html 

Or page http://www.freebuf.com/network/137662.html

![](https://raw.githubusercontent.com/ssooking/AutoBeef/master/autobeef.png) 

You should modify the code to satisfy your beef platform,such as the beef host url , the module's id . You can add autorun modules you want,and add exception handling to make these codes more robust.Test code for each individual module are stored in folder "test"，you can test it before you add into AutoBeef

  实验需要而写的一个简单小程序，可以自动控制被hook的主机运行指定模块。使用之前你应该修改代码来适应你的beef平台，如主机的URL，模块的ID、参数等。你可以添加你想要自动运行的模块，并添加异常处理使这些代码更健壮。每个模块的独立测试代码在test目录下，目前实现的几个模块：执行javascript、创建隐藏iframe、浏览器页面重定向、关闭页面时延时确认。
