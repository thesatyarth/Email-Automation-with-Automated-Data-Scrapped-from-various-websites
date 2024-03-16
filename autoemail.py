#Code below sends an email to whomever through python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'jobsearchautomated@gmail.com'
receiver = 'thesatyarth@gmail.com', 'ak6468@srmist.edu.in','ts4285@srmist.edu.in', 'cringeusmile@gmail.com', 'pk382774@gmail.com'

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
s.login(user = 'jobsearchautomated@gmail.com', password = 'endf tywz rrgl juey')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'cringeusmile@gmail.com'
receiver = 'thesatyarth@gmail.com', 'ts4285@srmist.edu.in', 'pk382774@gmail.com'

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
s.login(user = 'jobsearchautomated@gmail.com', password = 'endf tywz rrgl juey')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'jobsearchautomated@gmail.com'
receiver = 'thesatyarth@gmail.com', 'ts4285@srmist.edu.in'

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
s.login(user = 'jobsearchautomated@gmail.com', password = 'endf tywz rrgl juey')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'jobsearchautomated@gmail.com'
receiver = 'thesatyarth@gmail.com'

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
s.login(user = 'jobsearchautomated@gmail.com', password = 'endf tywz rrgl juey')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'jobsearchautomated@gmail.com'
receiver = 'iam.anubhab18@gmail.com'

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
s.login(user = 'jobsearchautomated@gmail.com', password = 'endf tywz rrgl juey')
s.sendmail(sender, receiver, msg.as_string())
s.quit()

