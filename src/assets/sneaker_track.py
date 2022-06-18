from pyclbr import Class
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import io

page_data = []

site_link = 'https://www.nicekicks.com/sneaker-release-dates/'


def getPages(link):
    DRIVER_PATH = '../../../../chromedriver_win32/chromedriver'

    driver = webdriver.Chrome(DRIVER_PATH)

    driver.get(site_link)

    while(True):
        try:
                page = driver.page_source
                page_data.append(page)
                print('page added!')
                next_button = driver.find_elements(By.CSS_SELECTOR, 'nav ul li.pagination-next a')
                # print(next_button)
                # last_button = len(next_button) - 1
                # next = next_button[last_button]
                driver.execute_script("arguments[0].click();", next_button[0])
                time.sleep(3)

        except Exception:
            break

    with io.open('sneakdata.txt', 'w') as sneaktry:
        for p in page_data:
            getSneaks(p)
            # Have the getSneaks function return the actual page data and have
            # the file get written from the return object
            sneaktry.write(p)



    #print(page_data)

# Sneakdata.txt has the full website output with all the needed info
# but soup object is only looking at a page at a time and idk how that is
# affecting the parsing
def getSneaks(page):
    soup = BeautifulSoup(page, features='html.parser')
    for sneak in soup.findAll('article', class_='post-summary__footer'):
        print(sneak.contents[0])


if __name__ == '__main__':
    getPages(site_link)


# button structure
# li class= pagination-next
# a href = next link