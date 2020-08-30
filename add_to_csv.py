import parse
import os
import csv
from langdetect import detect


class ToCSV:

    def __init__(self, csv_file_name):
        if not os.path.isfile(csv_file_name):
            with open(csv_file_name, 'w', encoding='UTF-8', errors='ignore') as file:
                self.csv_writer = csv.writer(file)
                self.csv_writer.writerow(['link',
                                          'categories',
                                          'date_published',
                                          'date_modified',
                                          'headline',
                                          'short_description',
                                          'full_description',
                                          ])
        self.file_name = csv_file_name

    def csv_writerow(self, row):
        with open(self.file_name, 'a', encoding='UTF-8', errors='ignore') as file:
            self.csv_writer = csv.writer(file)
            self.csv_writer.writerow(row)

    def add(self, html_file_path):
        data = parse.Parse(html_file_path).get_data()
        # -1 is full_description, -2 is short_description, -3 is headline
        if (data[-1] or data[-2]) and data[-3] and detect(data[-3]) == 'en':
            self.csv_writerow(data)
