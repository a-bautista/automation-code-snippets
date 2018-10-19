''' Author: Alejandro Bautista Ramos
    Last modification date: March 18th, 2018 '''

# Python 3.5.2 and above
import logging
from datetime import datetime

# generate a log file with the current date  

LOG_FILENAME = 'C:\\Users\\user_X\\Desktop\\Development\\outputs\\logging_results_'+str(datetime.now()).split(' ')[0]+'.out'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.debug("This line will go to the log file you created.")