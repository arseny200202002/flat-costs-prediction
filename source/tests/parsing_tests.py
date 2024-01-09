import csv
from local_development.parser.parser import CianParser
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename="tests_log.log",filemode="w", encoding='utf-8')

class ParserTest(unittest.TestCase):
    def single_test_find_pagenum(self, city_id, correct_value):
        parser = CianParser(city=city_id)
        url = parser.create_url()
        max_page_number = parser.find_pagenum(url)
        self.assertEqual(max_page_number, correct_value)
    
    def multiple_test_find_pagenum(self):
        self.single_test_find_pagenum(city_id=1, correct_value=54)
        self.single_test_find_pagenum(city_id=2, correct_value=54)
    
    def test_parser(self):
        parser = CianParser(city=1, save_file_directory='source/tests/parser_test_data/')
        parser.parse()

    def test_create_url(self):
        parser = CianParser(city=1)
        url = parser.create_url()
        print(url)

    def test_parse_page(self):
        parser = CianParser(city=1, save_file_directory='source/tests/parser_test_data/')

        with open(f'source/tests/parser_test_data/test.csv', 'w', newline='', encoding='utf-8') as file:
            parser.writer = csv.writer(file)
            parser.parse_page(parser.url + '&p=1')

    def test_parse(self):
        parser = CianParser(city=1,
                            save_file_directory='source/tests/parser_test_data/',
                            debug=False)
        
        parser.parse()
