import csv
import datetime
import requests
from bs4 import BeautifulSoup as bs
import cloudscraper
import re
import logging

from .url_constants import *

BASIC_DATA_DIRECTORY = 'source/local_development/parser/received_data/'

def attempts(func):
    def inner(*args, **kwargs):
        result = 1
        for i in range(5):
            try:
                result = func(*args, **kwargs)
                break
            except:
                continue
        else:
            logging.warning(f"limit of connetions exceeded function name: {func.__name__}")
        return result
    return inner


class CianParser:
    def __init__(self, city,
                 save_file_directory=BASIC_DATA_DIRECTORY,
                 metro=None,
                 district=None):
        
        self.city = city
        self.metro = metro
        self.district = district

        self.scrapper = cloudscraper.create_scraper()
        self.writer = None
        self.save_file_directory = save_file_directory

        self.url = self.create_url()

    def navbar_inspection(self, url, page) -> tuple:
        url += PAGE.format(page)
        responce = self.scrapper.get(url).text
        soup = bs(responce, 'html.parser')

        navbar = soup.find(attrs={'data-name': 'Pagination'})
        li = navbar.find_all('li')

        second = li[1].find('span').text
        last = li[-1].find('span').text

        return second, last

    @attempts
    def find_pagenum(self, url):
        for page in range(1, 500, 100):
            second, last = self.navbar_inspection(url, page)

            if last.isnumeric():
                return last
            if int(second) == 2 and page > 1:
                max_page = page
                min_page = max_page - 100
                cur_page = (max_page + min_page)//2
                break
        else:
            logging.error("выход за пределы потолка количества страниц на сайте")
            return 1
        
        while True:
            second, last = self.navbar_inspection(url, cur_page)
            if last.isnumeric():
                return int(last)
            if second.isnumeric():
                max_page = cur_page
            else:
                min_page = cur_page

            cur_page = (max_page + min_page)//2

    #@attempts
    def parse_page(self, current_url):
        try:
            responce = self.scrapper.get(current_url).text
        except:
            logging.error('problem with requests')
            return

        soup = bs(responce, 'html.parser')

        offers = soup.find_all(attrs={'data-testid': 'offer-card'})

        logging.info(f'offers detected: {len(offers)}')

        for offer in offers:
            #landlord information
            realtor = offer.find('span', {'class': '_93444fe79c--color_gray60_100--mYFjS'}).text
            realtor_name = offer.find('span', {'class': '_93444fe79c--color_current_color--vhuGI'}).text

            #price information
            price_block = offer.find('div', {'class': '_93444fe79c--container--aWzpE'})
            string = price_block.find('span', {'class': ''}).text
            start, end = re.search(r'([0-9]+\s)+', string).span()
            price = int(''.join(string[start:end].strip().split()))

            if(re.match(r'/сутки', string)): price *= 30

            #metro
            metro = None
            try:
                metro_block = offer.find('a', {'class': '_93444fe79c--link--BwwJO'})
                metro = metro_block.find('div', {'class': ''}).text
            except:
                pass
            
            #district
            geo_info_block = offer.find('div', {'class': '_93444fe79c--labels--L8WyJ'})
            a_blocks = geo_info_block.find_all('a')
            block_text = [block.text for block in a_blocks]

            district = None
            for text in block_text:
                if re.match(r'^р-н', text):
                    district = ' '.join(text.split()[1:])
                if re.match(r'[0-9]+/[0-9]+', text):
                    floor, max_floor = map(int, text.split('/'))
            
            #main info
            try:
                text = subtitle = offer.find('span', {'data-mark': 'OfferSubtitle'}).text
            except:
                title = offer.find('span', {'data-mark': 'OfferTitle'})
                text =  title.find('span', {'class': ''}).text
                
            info = text.split()
            
            start, end = re.search(r', [0-9]+,?[0-9]+ м', text).span()
            area = float(text[start+2:end-1].replace(',', '.'))

            if('студия' in info[0].lower()):
                rooms = 0
            else:
                try: 
                    rooms = int(info[0][0])
                except:
                    continue

            flat_type = info[1][:-1]

            new_flat = [price,
                        flat_type,
                        area,
                        rooms,
                        floor,
                        max_floor,
                        district,
                        metro,
                        realtor,
                        realtor_name
                        ]

            self.writer.writerow(new_flat)

    def create_url(self):
        url = BASE_LINK
        url += ALL_ROOMS
        url += STUDIO
        url += DEAL_TYPE.format(DEAL_TYPES['аренда'])
        url += ACCOMMODATION_TYPE_PARAMETER.format(ACCOMMODATION_TYPES['квартира'])

        url += CITY.format(self.city)

        if self.metro:      url += METRO.format(self.metro)
        if self.district:   url += DISTRICT.format(self.district)

        return url

    def parse(self):
        #find number of pages
        #pagenum = self.find_pagenum(self.url + PAGE.format(1))

        pagenum = 2

        today = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

        with open(f'{self.save_file_directory}cian-{today}.csv', 'w', newline='', encoding='utf-8') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(FIELDS)

            for page in range(1, pagenum + 1):
                self.parse_page(self.url + PAGE.format(page))

if __name__ == "__main__":
    parser = CianParser(city=1)
    parser.parse()



    