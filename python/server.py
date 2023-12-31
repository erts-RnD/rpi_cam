#!/usr/bin/python3

import cv2, socket, numpy, pickle  

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  # Gives UDP protocol to follow
ip="10.42.0.1"   # Server public IP
port=5000             # Port number should be same for both server and client
s.bind((ip,port))     # Bind the IP:port to connect 

# In order to iterate over block of code as long as test expression is true
while True:
    x=s.recvfrom(100000000)    # Recieve byte code sent by client using recvfrom
    clientip = x[1][0]         # x[1][0] in this client details stored,x[0][0] Client message Stored
    data=x[0]                  # Data sent by client
    data=pickle.loads(data)    # All byte code is converted to Numpy Code 
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)  # Decode 
    data = cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
    cv2.imshow('my pic', data) # Show Video/Stream
    if cv2.waitKey(10) == 13:  # Press Enter then window will close
        break
cv2.destroyAllWindows()        # Close all windows
