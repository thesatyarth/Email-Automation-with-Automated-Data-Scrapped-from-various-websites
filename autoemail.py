#Code below sends an email to whomever through python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = '__________________@gmail.com'
receiver = '_______________@gmail.com', '___________@srmist.edu.in','_____________@srmist.edu.in', '___________@gmail.com', '_________@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Data Analyst Internships Available'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('D:/Project1244/Data Analyst Internship.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="Data Analyst Internship.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '____________@gmail.com', password = '*******')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = '______________@gmail.com'
receiver = '_________________@gmail.com', '______@srmist.edu.in', '______________@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Data Science Internships Available'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('D:/Project1244/Data Science Internship.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="Data Science Internship.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '______________@gmail.com', password = '**********')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = '_____________@gmail.com'
receiver = '__________@gmail.com', '_________@srmist.edu.in'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Frontend Developer Internships Available'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('D:/Project1244/Frontend Developer Internship.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="Data Science Internship.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '________________-@gmail.com', password = '**********')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = '_________________@gmail.com'
receiver = '________________@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Backend Developer Internships Available'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('D:/Project1244/Backend Developer Internship.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="Data Science Internship.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '_________________@gmail.com', password = '*************')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = '_______________@gmail.com'
receiver = '_____________@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'App Developer Internships Available'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('D:/Project1244/App Developer Internship.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="Data Science Internship.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '_________________@gmail.com', password = '*************')
s.sendmail(sender, receiver, msg.as_string())
s.quit()

