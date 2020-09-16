from socket import *
#AF_INET ipv4
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a socketserver
serverSocket.bind(('', 6789))   #bind socket to 6789 port
serverSocket.listen(1)  #max connect user set to 1
#

#establish connection 
while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept() #accept client http request and build new socket
    try:
        message = connectionSocket.recv(1024)
        print(message)                          #message is http package
        filename = message.split()[1]           #tend to http package filename is '/HelloWorld.html'
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        #for i in range(0, len(outputdata)):
        #    connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        header = ' HTTP/1.1 404 Found'
        connectionSocket.send(header.encode())

        #Close client socket
        connectionSocket.close()
serverSocket.close()