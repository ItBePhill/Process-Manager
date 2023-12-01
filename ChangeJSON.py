#ChangeJson.py, will be what actually changes the file which Main.py reads from, since I want a GUI and console app
#Ver 0.1
import json
import os
import logging
logging.basicConfig(filename='ChangeJson.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logging.info("Started ChangeJSON Successfully!")
file = os.path.join(os.path.dirname(__file__), "processes.json")
def Edit(change):
    logging.info(f"Changing file to: {change}")
    try:
        with open(file, "r+") as f:
            json.dump(change, f)
    except Exception as e:
        logging.error(f"Something Went Wrong:", exc_info= e)
        return None

    logging.info(f"Successfully Changed to: {change}")
    