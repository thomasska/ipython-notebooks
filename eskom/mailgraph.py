#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = 'tabbott@ska.ac.za'
toaddr = 'tabbott@ska.ac.za'
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Eskom graph"
 
body = "Please see attached graph"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "latestgraph.png"
attachment = open("latestgraph.png", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.kat.ac.za')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
