#!/usr/bin/env python


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# create the message body
msg = MIMEText('Hello Thomas, here\'s a test email from Python on kat-imager2')

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Test email from Python'
msg['From'] = 'tabbott@ska.ac.za'
msg['To'] = 'tabbott@ska.ac.za'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.kat.ac.za')
s.sendmail('tabbott@ska.ac.za', 'tabbott@ska.ac.za', msg.as_string())
s.quit()




# an email with a file attachment

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Test email with an attachment'
msg['From'] = 'tabbott@ska.ac.za'
msg['To'] = 'tabbott@ska.ac.za'
msg.preamble = 'Here is the body / preamble of the message'

body = 'Here is a message body\n\nAnd a new line?\n\n\n Bye, Thomas'

msg.attach(MIMEText(body, 'plain'))

pngfiles=['Correlator Compiling.png','Power Detection.png']
# Assume we know that the image files are all in PNG format
for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

# Send the email via our own SMTP server.
s = smtplib.SMTP('smtp.kat.ac.za')
s.sendmail('tabbott@ska.ac.za', 'tabbott@ska.ac.za', msg.as_string())
s.quit()

