'''
Author: Amit Chakraborty
Project: Replica-watch Forum Thread Data Scraper
Profile URL: https://github.com/amitchakraborty123
E-mail: mr.amitc55@gmail.com
'''

from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from datetime import datetime

dt = str(datetime.now().strftime("%Y_%m_%d___[%I_%M_%S_%p]"))
warnings.filterwarnings("ignore")

class MyUDC(uc.Chrome):
    def __init__(self, *args, **kwargs):
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        # options.add_argument('--blink-settings=imagesEnabled=false')    # Disable images
        super(MyUDC, self).__init__(options=options, *args, **kwargs)
    def __del__(self):
        try:
            self.service.process.kill()
        except:
            pass

        
def scrape_data():
    # url = "https://forum.replica-watch.info/threads/bad-gateway-502-does-anyone-see-the-same.10981213/"
    url = input("Input your thread url: ")
    max_page = int(input('How many pages do you want to scrap: '))
    driver = MyUDC()
    driver.maximize_window()
    page = 0
    while True:
        page += 1
        if page > max_page:
            break
        print(f"Getting page {page} out of {max_page}")
        main_url = f'{url}page-{page}'

        driver.get(main_url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        try:
            lis = soup.find('div', {'class': 'js-replyNewMessageContainer'}).find_all('article', {'class': 'message--post'})
        except:
            lis = []
        print("Listing here: ", len(lis))
        if len(lis) < 1:
            break
        if len(lis) > 0:
            for li in lis:
                reply_time = ''
                name = ''
                pro_img = ''
                job_title = ''
                user_title = ''
                joined = ''
                messages_count = ''
                reaction_count = ''
                points_count = ''
                post = ''
                location = ''
                message_text = ''
                try:
                    reply_time = li.find('ul', {'class': 'message-attribution-main'}).find('time').text.replace('\n', '').strip()
                except:
                    pass
                try:
                    pro_img = "https://forum.replica-watch.info" + li.find('div', {'class': 'message-avatar'}).find('img')['src']
                except:
                    pass
                try:
                    name = li.find('h4', {'class': 'message-name'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    job_title = li.find('div', {'itemprop': 'jobTitle'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    user_title = li.find('h5', {'class': 'message-userTitle'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    des = li.find('div', {'class': 'message-userExtras'}).find_all('dl')
                    for dess in des:
                        if '<i aria-hidden="true" class="fa--xf far fa-user"></i>' in str(dess):
                            joined = dess.find('dd').text.replace('\n', '').strip()
                        if '<i aria-hidden="true" class="fa--xf far fa-comments"></i>' in str(dess):
                            messages_count = dess.find('dd').text.replace('\n', '').strip()
                        if '<i aria-hidden="true" class="fa--xf far fa-thumbs-up"></i>' in str(dess):
                            reaction_count = dess.find('dd').text.replace('\n', '').strip()
                        if '<i aria-hidden="true" class="fa--xf far fa-trophy"></i>' in str(dess):
                            points_count = dess.find('dd').text.replace('\n', '').strip()
                        if '<i aria-hidden="true" class="fa--xf far fa-map-marker"></i>' in str(dess):
                            location = dess.find('dd').text.replace('\n', '').strip()
                except:
                    pass
                try:
                    message_text = li.find('div', {'class': 'message-userContent'}).text.replace('\n', '').strip()
                except:
                    pass
                data = {
                    'Name': name,
                    'User Title': user_title,
                    'Post Time': reply_time,
                    'Profile Image': pro_img,
                    'Job Title': job_title,
                    'Joined': joined,
                    'Message Count': messages_count,
                    'Reaction Count': reaction_count,
                    'Points Count': points_count,
                    'Posts': post,
                    'Location': location,
                    'Message Content': message_text
                }
                df = pd.DataFrame([data])
                df.to_csv('Data___(' + dt + ').csv', mode='a', header=not os.path.exists('Data___(' + dt + ').csv'), encoding='utf-8-sig', index=False)
    driver.close()

if __name__ == '__main__':
    scrape_data()
    print('=============  All Data Scraped Successfully  =============')