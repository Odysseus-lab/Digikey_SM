# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:28:10 2024

@author: odysseus.valdez
"""

import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import win32com.client
import ctypes # for the VM_QUIT to stop PumpMessage()
import pythoncom
import re
import time
import psutil

