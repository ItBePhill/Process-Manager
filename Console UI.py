#Console UI.py, Will be what gives Main.py what needs to be changed
#Ver 0.1
import logging
from datetime import date
import os
logpath = os.path.join(os.path.dirname(__file__), "Logs")
logs = len(os.listdir(logpath))

if not os.path.exists(logpath):
    os.makedirs(logpath)
from ChangeJSON import *
logging.basicConfig(filename=f'{logpath}\{logs+1}{date.today()} Log.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logging.info("Started Console UI Successfully!")