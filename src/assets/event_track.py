from bs4 import BeautifulSoup
import json
from dataclasses import dataclass, field
from datetime import datetime
import io
from lists import cityList, chicago_venue_list, philly_venue_list, los_angeles_venue_list, nyc_venue_list
from selenium import webdriver
from selenium.webdriver.common.by import By


import time


@dataclass
class Event:
    name: str
    venue: str
    time: str
    link: str

data = {}
chicago_data = {}
data['chicago'] = []
data['los-angeles'] = []
data['philly'] = []
data['nyc'] = []

def scrapeEvents(city):
    venue_list = []
    if city == 'chicago':
        venue_list = chicago_venue_list
    elif city == 'los-angeles':
        venue_list = los_angeles_venue_list
    elif city == 'nyc':
        venue_list = nyc_venue_list
    else:
        venue_list = philly_venue_list
    
    for venue in venue_list:
        page_source = smashScrollButton(venue)

        soup = BeautifulSoup(page_source, features='html.parser')
        for script_tag in soup.findAll('script', type='application/ld+json'):
            json_obj = json.loads(script_tag.contents[0])
            if 'Date' in json_obj['startDate']:
                date = 'DATE TBA'
                e = Event(json_obj['name'], json_obj['location']['name'], date, json_obj['url'])
            else:
                split_date = json_obj['startDate'].split('T')[0].split('-')
                date = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
                e = Event(json_obj['name'], json_obj['location']['name'], date.ctime(), json_obj['url'])
            data[city].append({
                'name': e.name,
                'venue': e.venue,
                'time': e.time,
                'link': e.link
            })

def smashScrollButton(venue):
    asf = ''
    DRIVER_PATH = '../../../../chromedriver_win32/chromedriver'

    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)    

    driver = webdriver.Chrome(DRIVER_PATH)
    
    driver.get(venue)
    SCROLL_PAUSE_TIME = 0.5
    height = driver.execute_script("return document.body.scrollHeight") 

    while True:
        scrollh = height * 0.6
        driver.execute_script("window.scrollTo(0, arguments[0]);", scrollh)
        time.sleep(2)
        try:
            all_buttons = driver.find_element(By.CSS_SELECTOR, 'a.show-more')
            time.sleep(1)
            driver.execute_script("arguments[0].click();", all_buttons)
            time.sleep(2)
        except Exception:
            break
        height = driver.execute_script("return document.body.scrollHeight")

    page = driver.page_source

    return page
            
if __name__ == '__main__':
    for city in cityList:
        scrapeEvents(city)

    with io.open('data.json', 'w', encoding='utf-8') as json_data:
        json.dump(data, json_data)