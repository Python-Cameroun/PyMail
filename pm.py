# PM is a simple mail API
# Using an existing smtp configuration
# By Sanix darker
# PYTHON-CAMEROUN

import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'USERNAME or EMAIL ADDRESS'
password = 'PASSWORD'
sender = 'ME@EXAMPLE.COM'
targets = ['HE@EXAMPLE.COM', 'SHE@EXAMPLE.COM']

msg = MIMEText('How mbom, xa dit quoi?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()