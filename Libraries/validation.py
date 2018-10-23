import os.path
from datetime import datetime, timedelta
import Send_email

def validate(admin_Emails):

	for filename in os.listdir('./inputfiles'):#Iterate through all files in inputfiles folder

		file_createdTime = datetime.fromtimestamp(os.path.getctime('./inputfiles/'+filename)).strftime('%Y-%m-%d %H:%M:%S')#File Creation time in specific format

		file_age = datetime.strptime(file_createdTime, '%Y-%m-%d %H:%M:%S')+ timedelta(hours = 24)#Adding 24hrs to file created time (file valid untill this time)

		now = datetime.now()#Current time

		if file_age > now:#Checking whether file valid or not
			ageStatus = True
		else:
			ageStatus = False
			print (filename + " is more than 24 hours")
			#Send_email.send_Email(filename,admin_Emails)
			#exit()		

	return ageStatus		
