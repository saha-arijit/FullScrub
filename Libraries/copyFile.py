import shutil
from os import path
import sys

class copyFile():
	def copy(self,inputFile):
		if path.exists(inputFile):
			src = path.realpath(inputFile);
		
		head, tail = path.split(src)
		
		dst = "./outputfiles/full.scrub.csv"
		# nowuse the shell to make a copy of the file
		shutil.copy(src, dst)
		
		#copy over the permissions,modification
		shutil.copystat(src,dst)

copy_file = copyFile()
copy_file.copy(sys.argv[1])


	
