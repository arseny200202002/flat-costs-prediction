import csv
import datetime
import requests
from bs4 import BeautifulSoup
from request_constants import *
import pandas as pd

class CianParser:
    def __init__(self):
        pass
    def create_csv():
        today = datetime.datetime.today().strftime('%Y_%M_%d')
        with open(f'source/local_development/parser/received_data/cian-{today}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            fields = FIELDS
            writer.writerow(fields)
            

    def parse(city_id, district_id):
        url = ''
        page = requests.get(url)
        print(page.status_code)

if __name__ == "__main__":
    parser = CianParser()
    parser.parse()