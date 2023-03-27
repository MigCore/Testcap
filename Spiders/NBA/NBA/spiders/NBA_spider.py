import scrapy as sc
import time
from bs4 import BeautifulSoup
class Seasonsspider(sc.Spider):
    name = 'Seasons'
# This parse grabs each season
    def start_requests(self):
        urls = ["https://www.basketball-reference.com/leagues/NBA_2016_games.html","https://www.basketball-reference.com/leagues/NBA_2017_games.html","https://www.basketball-reference.com/leagues/NBA_2018_games.html","https://www.basketball-reference.com/leagues/NBA_2019_games.html","https://www.basketball-reference.com/leagues/NBA_2020_games.html","https://www.basketball-reference.com/leagues/NBA_2021_games.html","https://www.basketball-reference.com/leagues/NBA_2022_games.html"]
        for link in urls:
            time.sleep(3)
            yield sc.Request(url=link,callback=self.parse)
    def parse(self, response):
        time.sleep(3)
        soup = BeautifulSoup(response.text,'lxml')
        months = soup.select('#content .filter')
        links =[]
        for link in months[0].find_all('a'):
            links.append('https://www.basketball-reference.com' + link.get('href'))
        for link in links:
            yield response.follow(url = link, callback= self.parse2)
# pasrse2 grabs the boxes for each season
    def parse2(self,response):
        time.sleep(3)
        soup = BeautifulSoup(response.text,'lxml')
        yield { "Season" : response.url,
        "Box Score" : soup.select('#all_schedule')
        }
        




