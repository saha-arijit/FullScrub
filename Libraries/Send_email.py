import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import logger

def send_Email(fileName,client_emails,sender_mail,sender_pwd):

	for mail in client_emails:
		msg = MIMEMultipart()
		msg['From'] = sender_mail
		msg['To'] = mail
		msg['Subject'] = 'Subject'
		message = 'Actual MSG'
		msg.attach(MIMEText(message))

		server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
		server.login(sender_mail, sender_pwd)

		server.sendmail(sender_mail,mail,msg.as_string())

		server.quit()