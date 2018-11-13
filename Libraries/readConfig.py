import logger

def readConfig():
	config_File = open('./Libraries/input_Files/configFile','r+')
	files = { }

	for line in config_File:

		if line == '':
			pass
		else:

			if '\n' in line:
				line = line.split('\n')[0]

			if ' ' in line:
				line = line.replace(' ','')

			if 'tcsInputFile' in line:
				files['tcsInputFile'] = line.split('tcsInputFile:')[1]
			elif 'FIBEInputFile' in line:
				files['FIBEInputFile'] = line.split('FIBEInputFile:')[1]
			elif 'AliantInputFile' in line:
				files['AliantInputFile'] = line.split('AliantInputFile:')[1]
			elif 'VCMInputFile' in line:
				files['VCMInputFile'] = line.split('VCMInputFile:')[1]
			elif 'VSSAInputFile' in line:
				files['VSSAInputFile'] = line.split('VSSAInputFile:')[1]
			elif 'IPVODInputFile' in line:
				files['IPVODInputFile'] = line.split('IPVODInputFile:')[1]
			elif 'AdminEmail' in line:
				files['AdminEmail'] = line.split('AdminEmail:')[1]
			elif 'log' in line:
				files['log'] = line.split('log:')[1]
			elif 'sender_Id' in line:
				files['sender_Id'] = line.split('sender_Id:')[1]
			elif 'sender_password' in line:
				files['sender_password'] = line.split('sender_password:')[1]

	logger.MessageLog("Got information from conf file")
	return files
