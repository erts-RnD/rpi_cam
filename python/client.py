#!/usr/bin/python3

import time
import cv2, socket, pickle, os
from picamera2 import Picamera2, Preview

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000) 
serverip="10.42.0.1"       # IP address of ROS master (PC)
serverport=5000              # Port number should be same for client and server


picam2 = Picamera2()
#picam2.start_preview(Preview.QT)
#preview_config = picam2.create_preview_configuration()
#picam2.configure(preview_config)

picam2.start()
#time.sleep(65)

while True:
	im = picam2.capture_array()
	ret, buffer = cv2.imencode(".jpg", im, [int(cv2.IMWRITE_JPEG_QUALITY),30])  # ret will returns whether connected or not, Encode image from image to Buffer code(like [123,123,432....])
	x_as_bytes = pickle.dumps(buffer)       # Convert normal buffer Code(like [123,123,432....]) to Byte code(like b"\x00lOCI\xf6\xd4...")
	s.sendto(x_as_bytes,(serverip , serverport)) # Converted byte code is sending to server(serverip:serverport)