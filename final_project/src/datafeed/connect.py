import os
from dotenv import dotenv_values
PYTHONPATH = dotenv_values(".env")["PYTHONPATH"]

DATAPATH = os.path.join(PYTHONPATH, "data")
