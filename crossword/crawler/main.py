from environ import *
from crawler import *
from logger import *
from time import sleep

class MainCrawler():
    while True:
        logger.info(f"{APP_NAME} crawler has started")
        Crawler()
        logger.info(f"{APP_NAME} crawler has finished. \nData sent to 'data.json' file ")
        sleep(SLEEP)
