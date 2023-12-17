#ChangeJson.py, will be what actually changes the file which Main.py reads from, since I want a GUI and console app
#Ver 0.1
import json
import os
import logging
from datetime import date
logpath = os.path.join(os.path.dirname(__file__), "Logs")
logs = len(os.listdir(logpath))
logging.basicConfig(filename=f'{logpath}\{date.today()} Log.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logging.info("Started ChangeJSON Successfully!")



file = os.path.join(os.path.dirname(__file__), "processes.json")
if not os.path.exists(file):
    logging.info("file not found creating processes.json")
    try:
        with open("processes.json", "w") as f:
            json.dump({}, f)
    except Exception as e:
        logging.error("Something Went Wrong:", exc_info=e)
        quit(0)
    logging.info("Successfully created processes.json")

def Edit(change):
    logging.info(f"Changing file to: {change}")
    try:
        with open(file, "w") as f:
            json.dump(change, f)
    except Exception as e:
        logging.error(f"Something Went Wrong:", exc_info= e)
        return None

    logging.info(f"Successfully Changed to: {change}")
    
def Delete():
    logging.info(f"Deleting processes.json")
    try:
        os.remove(file)
    except Exception as e:
        logging.error("Something Went Wrong:", exc_info = e)
        return None
    
    logging.info("Successfully Deleted Processes.json")