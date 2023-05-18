import pandas as pd
from sqlalchemy import create_engine

# 1. Read data from csv using pandas
data_df = pd.read_csv('data.csv')
subject_df = pd.read_csv('subject.csv')

# 2. Transform the value2 column data of data.csv file by making square of values
data_df['value2'] = data_df['value2'] ** 2

# 3. Save the transformed data in MySQL for both the files
user = 'root'
password = 'Kaletha%40123'
host = 'localhost'
database = 'heta_datain'

engine = create_engine(f'mysql://{user}:{password}@{host}/{database}')
data_df.to_sql('data', engine, if_exists='replace', index=False)
subject_df.to_sql('subject', engine, if_exists='replace', index=False)

# 4. Showcase relationship between data.csv and subject.csv file into third file named result.csv
result_df = pd.merge(data_df, subject_df, on='Subject_id')
result_df.to_csv('result.csv', index=False)

# Save result.csv into database
result_df.to_sql('result', engine, if_exists='replace', index=False)


# Showcase relationship between data.csv and subject.csv file into third file named result.csv
result_df = pd.merge(data_df, subject_df, on='Subject_id')

# Save result.csv
result_df.to_csv('result.csv', index=False)