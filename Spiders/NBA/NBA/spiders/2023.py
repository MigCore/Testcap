import scrapy as sc
import time
from bs4 import BeautifulSoup
class Seasonsspider(sc.Spider):
    name = 'Current'
# This parse grabs each season
    def start_requests(self):
        urls = ["https://www.basketball-reference.com/leagues/NBA_2023_games-october.html","https://www.basketball-reference.com/leagues/NBA_2023_games-november.html","https://www.basketball-reference.com/leagues/NBA_2023_games-december.html","https://www.basketball-reference.com/leagues/NBA_2023_games-january.html"]
        for link in urls:
            yield sc.Request(url=link,callback=self.parse)
            
# pasrse2 grabs the boxes for each season
    def parse(self,response):
        time.sleep(3)
        soup = BeautifulSoup(response.text,'lxml')
        yield { "Season" : response.url,
        "Box Score" : soup.select('#all_schedule')
        }
        




