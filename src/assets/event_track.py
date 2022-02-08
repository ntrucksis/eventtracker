import requests
from bs4 import BeautifulSoup
import json
from dataclasses import dataclass, field
from datetime import datetime
import urllib.request
import io
from lists import cityList
from selenium import webdriver
from selenium.webdriver.common.by import By


import time

aragon_url = 'https://www.livenation.com/venue/KovZpZAFdJnA/byline-bank-aragon-ballroom-events'
chi_theatre_url = 'https://www.livenation.com/venue/KovZpZA6AJ6A/the-chicago-theatre-events'
house_blues_url = 'https://www.livenation.com/venue/KovZpZAEAIlA/house-of-blues-chicago-events'
hb_pavilion_url = 'https://www.livenation.com/venue/KovZpZAEA7IA/huntington-bank-pavilion-at-northerly-island-events'
subtarranean_url = 'https://www.livenation.com/venue/KovZpZA1EktA/subterranean-events'

observatory_url = 'https://www.livenation.com/venue/KovZpZAF6JkA/the-observatory-events'
echo_url = 'https://www.livenation.com/venue/KovZ917A967/the-echo-events'
orpheum_url = 'https://www.livenation.com/venue/KovZpa3uCe/orpheum-theatre-events'
morrocan_url = 'https://www.livenation.com/venue/KovZ917AJ5H/the-moroccan-lounge-events'
palladium_url = 'https://www.livenation.com/venue/KovZpZAEAlaA/hollywood-palladium-events'
# forum

fillmore_url = 'https://www.livenation.com/venue/KovZpZAEkteA/the-fillmore-philadelphia-events'
tla_url = 'https://www.livenation.com/venue/KovZpZAEAIaA/theatre-of-living-arts-events'
camden_url = 'https://www.livenation.com/venue/KovZpZAEAIEA/bb-t-pavilion-events'
td_pavilion_url = 'https://www.livenation.com/venue/KovZpZAEdFJA/td-pavilion-at-the-mann-events'
foundry_url = 'https://www.livenation.com/venue/KovZpZAEktdA/the-foundry-events'
wells_fargo_url = 'https://www.livenation.com/venue/KovZpZAF6FtA/wells-fargo-center-events'

beacon_url = 'https://www.livenation.com/venue/KovZpZAEAd6A/beacon-theatre-events'
radio_city_url = 'https://www.livenation.com/venue/KovZpZAE7vdA/radio-city-music-hall-events'
irving_url = 'https://www.livenation.com/venue/KovZpaFPje/irving-plaza-events'
# webster_url = ''
# terminal5_url = ''


chicago_venue_list = [aragon_url, chi_theatre_url, house_blues_url, hb_pavilion_url, subtarranean_url]
los_angeles_venue_list = [observatory_url, echo_url, orpheum_url, morrocan_url, palladium_url]
philly_venue_list = [fillmore_url, tla_url, camden_url, td_pavilion_url, foundry_url, wells_fargo_url]
nyc_venue_list = [beacon_url, radio_city_url, irving_url]

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

        #event = requests.get(venue)
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

    

    driver = webdriver.Chrome(DRIVER_PATH)

    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
    
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
        


    # time.sleep(1)
    # new_height = driver.execute_script("return document.body.scrollHeight")
    # try:
    #     all_buttons = driver.find_element(By.CSS_SELECTOR, 'a.show-more')
    #     time.sleep(1)
    #     driver.execute_script("arguments[0].click();", all_buttons)
    #     time.sleep(1)
    # except Exception:
    #     pass

    # scrollh += 1500
    # driver.execute_script("window.scrollTo(0, arguments[0]);", scrollh)
    # time.sleep(2)
    # try:
    #     all_buttons = driver.find_element(By.CSS_SELECTOR, 'a.show-more')
    #     time.sleep(2)
    #     driver.execute_script("arguments[0].click();", all_buttons)
    #     time.sleep(2)
    # except Exception:
    #         pass

    page = driver.page_source
    # with io.open('test.txt', 'w') as file:
    #     file.write(page)

    return page

    # for x in range(len(all_buttons)):
    #     if all_buttons[x].is_displayed():
            


if __name__ == '__main__':
    #smashScrollButton(aragon_url)

    for city in cityList:
        scrapeEvents(city)

    with io.open('data.json', 'w', encoding='utf-8') as json_data:
        json.dump(data, json_data)


