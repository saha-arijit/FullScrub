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
	packageIdMatch.create_csv()

	print("Completed")

	
if __name__ == '__main__':
	FullScrub()
