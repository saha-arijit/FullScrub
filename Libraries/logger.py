import logging
import time 
import sys
import os
from logging.handlers import TimedRotatingFileHandler
import inspect	
import readConfig

def LoggerMethod(message):

	config_File = readConfig.readConfig()

	if os.path.isdir("./Log"):
		pass
	else:
		os.mkdir("./Log")
		
	if config_File['log'] == 'NO':
		log_file_name = "./Log/execution.log"
		logging_level = logging.INFO
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %I:%M:%S %p')
		handler=logging.FileHandler(log_file_name,mode='w')
		handler.setFormatter(formatter)
		logger = logging.getLogger()
		logger.addHandler(handler) 
		logger.setLevel(logging.INFO)

	elif config_File['log'] == 'YES':
		log_file_name = "./Log/"+'execution_'+time.strftime("%Y%m%d",time.localtime())+".log"
		logging_level = logging.INFO
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %I:%M:%S %p')
		handler = TimedRotatingFileHandler(log_file_name,when="midnight")
		handler.setFormatter(formatter)
		logger = logging.getLogger()
		logger.addHandler(handler) 
		logger.setLevel(logging.INFO)
	
def MessageLog(message):

    func = inspect.currentframe().f_back.f_code
    filename = func.co_filename.split('\\')
    logging.info("%s -> %s :: %s" % (filename[len(filename)-1],func.co_name,message))
	
def ErrorLog(message):

    func = inspect.currentframe().f_back.f_code
    filename = func.co_filename.split('\\')
 
    logging.error("%s -> %s :: %s" % (filename[len(filename)-1],func.co_name,message ))



