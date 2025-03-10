from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from utils import load_env
import os

env_vars = load_env()
DATABASE_URL = env_vars['PSQL']

path = './data/raw'

engine = create_engine(DATABASE_URL)

try:    
    for file in os.listdir(path):
        if file.endswith('.csv'):
            file_name = file[:-4]
            file_path = os.path.join(path, file)
            file_path = file_path.replace("\\", "/")

            df = pd.read_csv(file_path)
            
            df.to_sql(file_name, engine, if_exists='replace', index=False)

            print(f'✅ {file} uploaded as {file_name} to the DB.')
    print('🏁🏎️💨 All tables have been created')
except Exception as e:
        print(f"An error occurred: {e}")