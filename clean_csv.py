import pandas as pd
import os


class CleanCSV:
    def __init__(self, csv_file_name):
        if os.path.isfile(csv_file_name):
            df = pd.read_csv('data.csv')
            df = df.drop_duplicates(subset='link')
            df = df.sort_values('date_published')
            df.to_csv('data.csv', index=False)
