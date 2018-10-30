import sys
import os
sys.path.insert(0, "./Libraries")
import packageIdMatch

def FullScrub():

	print("Running.......")

	"""
			Function Name        : create_csv
			Function Description : creates the output file
			Inputs   : 
			Outputs  : 
				creates a .csv file
				
	""" 
	outputfile_name = packageIdMatch.create_csv()

	os.system('python ./Libraries/copyFile.py '+outputfile_name)

	print("Completed")


if __name__ == '__main__':
	FullScrub()
