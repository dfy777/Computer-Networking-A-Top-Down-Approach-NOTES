了解了socket的建立，连接，处理过程，实现了在本机通过http请求服务器并返回html的功能

接受到的报文
b'GET /HelloWorld.html HTTP/1.1\r\nHost: 123.206.203.167:6787\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,ru;q=0.6\r\nConnection: close\r\n\r\n'
