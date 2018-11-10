import sys
import os
from datetime import datetime
sys.path.insert(0, "./Libraries")
import packageIdMatch
import logger

def FullScrub():

	loggerTest = logger.LoggerMethod('name')
	logger.MessageLog("Execution Started")
	print("Running......." ,datetime.now())

	"""
			Function Name        : create_csv
			Function Description : creates the output file
			Inputs   : 
			Outputs  : 
				creates a .csv file
				
	""" 
	packageIdMatch.create_csv()

	#os.system('python ./Libraries/copyFile.py '+outputfile_name)

	print("Completed" , datetime.now())
	logger.MessageLog("Execution Completed")

if __name__ == '__main__':
	FullScrub()
