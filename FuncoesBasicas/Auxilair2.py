import pandas as pd
import sqlalchemy as sa
import numpy as np
import csv
from datetime import datetime
import warnings
from re import search
warnings.simplefilter("ignore")

# Create connection with database HOMOLOG
#engine = sa.create_engine('mysql+pymysql://wagner:WTK:MPN=]O${)SC@mysqlleads.cqgxnlyz0qdr.us-east-2.rds.amazonaws.com/dbleads')

# Create connection with database LOCALHOST (DUMP FROM HML)
engine = sa.create_engine('mysql+pymysql://root:Wagner25@localhost/dbleads')

# Create connection with database LOCALHOST V2.0
#engine = sa.create_engine('mysql+pymysql://root:Wagner25@localhost/leadsapi2.0')

cursor = engine.connect()
print('Connection established')
