#!/usr/bin/env python

import smtplib
import os.path
import time
from email.mime.text import MIMEText

# send me an email
def warnthomas(subj,body):
    msg = MIMEText(body)
    msg['Subject'] = subj
    msg['From'] = 'tabbott@ska.ac.za'
    msg['To'] = 'tabbott@ska.ac.za'
    s = smtplib.SMTP('smtp.kat.ac.za')
    s.sendmail('tabbott@ska.ac.za','tabbott@ska.ac.za', msg.as_string())
    s.quit()

    msg = MIMEText(body)
    msg['Subject'] = subj
    msg['From'] = 'tabbott@ska.ac.za'
    msg['To'] = 'blunsky@ska.ac.za'
    s = smtplib.SMTP('smtp.kat.ac.za')
    s.sendmail('tabbott@ska.ac.za','blunsky@ska.ac.za', msg.as_string())
    s.quit()





# loop to keep checking for time
filetocheck='/var/kat/archive/data/MeerKATAR1/telescope_products/2016/04/01/1459521241.h5'
#filetocheck='file.txt'
laststate = False

print 'Archive test program. Checking file %s every 30 seconds. Started at %s' % (filetocheck,time.ctime())
warnthomas('Archive monitoring started at %s' % time.strftime('%H:%M'),'Archive test program. Checking file %s every 30 seconds. Started at %s' % (filetocheck,time.ctime()))

while True:
    if not os.path.exists(filetocheck) and laststate:
        print 'Archive failure, %s not found at %s' % (filetocheck,time.ctime())
        warnthomas('Archive Failure at %s' % time.strftime('%H:%M'),'Archive failure, %s not found at %s' % (filetocheck,time.ctime()))
        laststate = False
    if os.path.exists(filetocheck) and not laststate:
        print 'Archive has returned at %s' % time.ctime()
        warnthomas('Archive restored at %s' % time.strftime('%H:%M'),'Archive has returned at %s' % time.ctime())
        laststate = True

    time.sleep(2)


