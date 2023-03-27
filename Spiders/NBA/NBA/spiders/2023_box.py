import scrapy as sc
import pandas as pd 
from bs4 import BeautifulSoup
class Seasonsspider(sc.Spider):
    name = '2023'
# This parse grabs each season
    def start_requests(self):
        df =pd.read_csv('/Users/migcord/Springboard/Capstone/2022_2.csv',header=None)
        urls =df.iloc[:,0]
        for link in urls:
            yield sc.Request(url=link,callback=self.parse)
    def parse(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        yield {
            'Box_Score' : soup.select('#content')
        }