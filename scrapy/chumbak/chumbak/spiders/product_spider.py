import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time


class ClothesSpider(scrapy.Spider):
    name = "clothes"

    start_urls = [
        'https://www.chumbak.com/women-apparel/GY1/c/',
    ]

    def parse(self, response):
        url = response.url
        wd = webdriver.Firefox(executable_path="/home/rishi/Documents/geckodriver")
        wd.get(url)

        f = open('clothes.html', 'w')
        time.sleep(5)
        f.write(wd.page_source.encode('utf8'))
        time.sleep(5)
        f.close()
        wd.close()
