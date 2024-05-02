import os
from datetime import datetime


CURRENT_DIR = os.getcwd()
DATABASE_DIR = os.path.join(CURRENT_DIR, "main_database", "database")
START_DATA = datetime(2022, 12, 31)