# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:15:44 2024

@author: Odysseus Valdez
"""

import serial
import os, sys
import time
from datetime import datetime, timedelta
import minimalmodbus

class DigiKey_Monitor(minimalmodbus.Instrument(1, 1,'rtu')):
    
    def __init__(self, day):
        self.isOpen = False
        self.serial.timeout = 0.1
        #self.ip_address = "192.168.2.1"
        self.serial.port = "1"
        self.serial.baudrate = 19200
        self.serial.parity = None
        self.serial.bytesize = 8
        self.serial.stopbits = 1
        self.alternate = "00"
        self.timestamp_list = []
        self.date
        self.voltage
        self.current
       # self.power
       
    def getDate(self):
        return 
    
    #Connecting to DigiKey IX10
    def connect(self):
        if not self.isOpen:
            try: 
                self.serial = serial.Serial(port=self.serial.port, baudrate=self.serial.baudrate, bytesize=self.serial.bytesize, 
                                   parity=self.serial.parity, 
                                   stopbits=self.serial.stopbits, 
                                   timeout=self.serial.timeout, write_timeout=self.serial.timeout)
            
                self.isOpen = self.client.is_open
                self.client.flush()
                #self.status = self.checkStatus()
                
            except serial.SerialException:
                return "Unable to connect to the specified port"
        else:
            return "Already Connected"
    
    def disconnect(self):
         if self.isOpen:
             self.client.close()
             self.isOpen = self.client.is_open
             return 'Disconnected from power supply on %s' % self.ip_address
         else:
             return 'Power supply is already disconnected.'    
    
    def read_interval(self,initial):
        print(initial)
        
        next_recording = initial + \
                         timedelta(seconds = 30)
        self.time_stamp(initial)
        while(datetime.now() < next_recording):
            continue
        
    def read(self):
        initial = datetime.now()
        self.voltage = self.read_register(1,3,3,False)
        self.current = self.read_register(2,3,3,False)
        #self.power = self.read_register(3,3,3,False)
        self.read_interval(initial)
                         
    def time_stamp(self, dt):
        Alternate1 = "00"
        Alternate2 = "30"
        time_string = str(dt)
        i = 0
        Date_Array = []
        print(len(time_string))
        if (dt.second > 29):
            self.alternate = Alternate2
        for p in range(len(time_string)):
            Date_Array.append(time_string[p])
        for j in range(17,19):
            Date_Array[j] = self.alternate[i]
            i += 1
        if (self.alternate == Alternate1):
            self.alternate = Alternate2
        else:
            self.alternate = Alternate1
        
        self.convert(Date_Array)
        
    def convert(self, Date_Array): 
        self.date = ""
        for x in Date_Array:
            self.date += x
        self.timestamps()  
            
    def timestamps(self):
        self.timestamp_list.append(self.date)
        with open ("Readings.csv", "a") as f:
            f.write(str(self.datetime) + "," + str(self.voltage) + ","
                  + str(self.current))
        
if __name__=='__main__':
    
    Monitor = DigiKey_Monitor()
    while (True):
        try:
            Monitor.connect()
            Monitor.read()
            Monitor.disconnect()
        except serial.SerialException:
            continue

           
