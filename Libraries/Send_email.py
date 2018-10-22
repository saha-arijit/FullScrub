import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_Email(fileName,emails):

	for mail in emails:
		msg = MIMEMultipart()
		msg['From'] = 'From address'
		msg['To'] = mail
		msg['Subject'] = 'Subject'
		message = 'Actual MSG'
		msg.attach(MIMEText(message))

		server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
		server.login('From address', 'password')

		server.sendmail('From address',mail,msg.as_string())

		server.quit()