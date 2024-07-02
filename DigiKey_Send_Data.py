# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:16:45 2024

@author: Odysseus Valdez
"""

import serial
import os, sys
import time
from datetime import datetime, timedelta
import csv
import scp
import importlib.util
spec = importlib.util.spec_from_file_location(
    "E:\Z_Temp-Exchange\Odysseus\DigiKey IX10\DigiKey_Emailer.py")
pyModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pyModule)

class DigiKey_Monitor(pyModule.Emailer):
    
    def __init__(self):
        self.isOpen = False
        self.__timeout = 10
        self.ip_address = "192.168.2.1"
        self.port = "COM4"
        self.inputArray
    
    #Connecting to DigiKey IX10
    def connect(self):
         if not self.isOpen:
             arg = 'socket://'+self.ip_address+':'+self.port
             try:
                 #THIS IS AT THE TOP TOO: YOU HAVE TO TEST THIS TO MAKE SURE IT WORKS
                 self.client = serial.serial_for_url(arg,
                                                     timeout=self.__timeout,
                                                     write_timeout=self.__timeout)
                 self.isOpen = self.client.is_open
                 self.client.flush()
                 
                 #self.status = self.checkStatus()
                 
                 return True
                 
             except serial.SerialException:
                 return False
         else:
             return True
         
    def disconnect(self):
         if self.isOpen:
             self.client.close()
             self.isOpen = self.client.is_open
             return 'Disconnected from power supply on %s' % self.ip_address
         else:
             return 'Power supply is already disconnected.'
         
        
    def scan_readings(self):
        psRemoteInput = open("Readings.csv", "r", 1)
        with psRemoteInput as f:
            reader = csv.reader(f, delimiter=",")
            self.inputArray = list(reader)
        self.output()    
            
    def output(self):
        length = len(self.inputArray) / 3
        while(i < length)):
            for j in range(3):
                
            
    def read_interval(self):
        self.output()
        initial = datetime.now()
        next_recording = initial + \
                         timedelta(minutes = 60)
        self.time_stamp(initial)
        while(datetime.now() < next_recording):
            continue
                
            
if __name__=='__main__':
    
    Monitor = DigiKey_Monitor()
    Monitor.connect()
    
    command = "*IDN?"  # Query instrument identification
    response = Monitor.send_command(command)
    print("Instrument identification:", response)

           
