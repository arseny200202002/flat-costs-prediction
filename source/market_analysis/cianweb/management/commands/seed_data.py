from cianweb.models import *
from django.core.management.base import BaseCommand
from cianweb.request_constants import *

import logging

class Command(BaseCommand):
    help = 'Fills daatbase with test and constant data'

    def handle(self, *args, **kwargs):
        logging.basicConfig(filename='py_log.log', filemode='w', encoding='UTF-8')

        #Filling rooms table
        for i in range(1, 5):
            Rooms.objects.get_or_create(roomnum=i)

        #Filling cities table
        for city in (CITIES + OTHER_CITIES):
            City.objects.get_or_create(name=city[0], cian_id=city[1])

        #Filling metro table
        for city in METRO_STATIONS.keys():
            for metro in METRO_STATIONS[city]:
                city_id = None
                try: 
                    city_id=City.objects.get(name=city).pk
                except Exception as e:
                    logging.exception(f'Exceptoin:{e} city_name:{city}')
                
                if city_id is not None:
                    Metro.objects.get_or_create(name=metro[0],
                                                cian_id=metro[1],
                                                city_id=city_id)
                    
        
        
        