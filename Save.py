#Save.py, Will save the rules / actions to a file
import json
import os
import logs
logs.info("Save.py Started Successfully!")


def Save(data: dict):
    logs.info(str(data))
    with open(f"{os.path.dirname(__file__)}\Json\{len(os.listdir('Json'))}.json", "w") as f:
        json.dump(data, f)
        f.close()


