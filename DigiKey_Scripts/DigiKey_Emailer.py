# -*- coding: utf-8 -*-

"""
Notifications library for email, etc.
"""

# Import default libraries
import sys
sys.dont_write_bytecode = True

if sys.version_info.major<=2:
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEBase import MIMEBase
if sys.version_info.major>=3:
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    #from email.MIMEImage import MIMEImage
    
from email import encoders
from datetime import datetime as dt
from time import sleep
import numpy as np
import pandas as pd
import smtplib

# Import CFV Libraries
libDir = r'C:\GitHUb\CFV-Library'
if libDir not in sys.path:
    sys.path.append(libDir)

img_dir_fault = r'C:\GitHub\CFV-Library\Media\Fault'
img_dir_inprogress = r'C:\GitHub\CFV-Library\Media\In Progress'
img_dir_testcomplete = r'C:\GitHub\CFV-Library\Media\Test Complete'
img_dir_attention = r'C:\GitHub\CFV-Library\Media\Attention'

accounts = dict()
accounts['DataAlerts'] = {'Address':'dataalerts@cfvlabs.com',
                          'Password':'DAcfv2022!'}
accounts['InstrumentationGroup'] = {'odysseus.valdez@cfvlabs.com'
                                    'james.richards@cfvlabs.com',
                                    'douglas.robb@cfvlabs.com'}
class Emailer: 
    
    """
    Wrapper for the email functions
    """
    
    def __init__(self):
        
        '''
        Subject and Body text are provided as inputs.
        Default values are blank
        
        Attachments can be provided as a list of filepaths. 
        '''
        self.account = 'odysseus.valdez@cfvlabs.com'
        #self.distributionList = distList
        self.subject = 'Daily String Monitor Data'
        self.attachments = 'Readings.csv'
        self.bodyHTML = ''
        self.body = ''
        self.user = ''
        self.password = ''
        self.msg = ''
    
    def clear_html(self):
        self.bodyHTML = ''
    
    def build_html(self,txt):
        self.bodyHTML += '<html>'
        self.bodyHTML += '<body>'
        if isinstance(txt,list):
            for line in txt:
                self.bodyHTML += '<p>%s</p>' % line        
        else:
            self.bodyHTML += '<p>%s</p>' % txt
        self.bodyHTML += '</body>'
        self.bodyHTML += '</html>'
    
    def construct_message(self,body=''):
        if body != '':
            self.body = body
        else:
            self.body = self.bodyHTML
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        
        # Attachments
        for fpath in self.attachments:
            with open(fpath, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
            
            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)
            
        msg.attach(MIMEText(self.body, 'html'))
        self.msg = msg
        return msg

    def send_notification(self):
        '''
        Send message to self.distribution_list recipients  
        '''
        msg = self.msg
        msg['From'] = self.user
        
        for contact in self.distributionList:
            msg['To'] = contact
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.starttls()
            server.login(self.user,self.password)
            server.sendmail(self.user, contact, msg.as_string())
            server.quit()
            
    def AlertInstrumentationGroup(self):
        #Send an alert for nefarious data        
        return
    
    def fetchDailyData(self):
        date = dt.now()
        print (date)
        hour = date.hour
        minute = date.minute
        second = date.second
        time = str(hour) + ":" + str(minute) + ":" + str(second)
        print("Time:", time)
        self.clear_html()            
        self.build_html(txt=txt_lines)
        self.construct_message(body=self.bodyHTML)
        self.send_notification()
        
if __name__ == '__main__':
    
    
    Email = Emailer()
    #distList = distribution_list['development']
    
    #print('Current distribution list:')
    #for address in distList:
    #    print(' %s' % address)
    
    txt_subject = ''
    #txt_body = '<html><i>This is a test.</i></html>'
    txt_lines = []
    txt_lines.append('')
    Email.fetchDailyData()
    
    