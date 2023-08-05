#!/usr/bin/env python
# coding: utf-8

# In[181]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pprint
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import chromedriver_autoinstaller 
import requests
from requests import get
import numpy as np


# In[225]:


import pymongo
from pymongo import MongoClient

uri = "mongodb+srv://juro9484:24October00@vividseats.2ks3snm.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# In[119]:


list_of_user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                       'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1',
                       'Mozilla/5.0 (iPod; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1',
                       'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                       'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                       'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                       'Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                       'Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                       'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
                       'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
                       ''
                      ]

new_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
             'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1',
              'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1',
              'Mozilla/5.0 (iPod; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1',
              'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
             ]

def agent_random():
    agent = random.choice(new_agents)
    return agent
        


# In[237]:



    response = requests.get(
    "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=100",
    headers={"Authorization": "dpmqaazul1il0snzb31sgyric9plmfbuezeuth32"}
    )
    
    array_of_proxies = []

    # response.json()
    for i in response.json()['results']:
    #     if i['country_code'] == 'US':
        array_of_proxies.append(str(i['proxy_address'])+":"+str(i['port']))

    def rand_proxy():
        proxy = random.choice(array_of_proxies)
        return proxy
    



    def webdriver_tickets2(state, city, date):
        global tickets_dict
        tickets_dict = []
        chromedriver_autoinstaller.install() 
        # Create Chromeoptions instance 
        options = webdriver.ChromeOptions()
        service = Service()
        # Adding argument to disable the AutomationControlled flag 
        options.add_argument("--disable-blink-features=AutomationControlled") 
        # Exclude the collection of enable-automation switches 
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        # Turn-off userAutomationExtension 
        options.add_experimental_option("useAutomationExtension", False) 
        # Setting the driver path and requesting a page 
        proxy = rand_proxy()
        options.add_argument(f'--proxy-server={proxy}')
        driver = webdriver.Chrome(options=options, service=service)
        driver.get('https://www.vividseats.com/region/usa/'+state+'/'+city+'-tickets/40/concerts?startDate='+date+'&endDate='+date+'/')

        list_of_artists = []
        list_of_dates = []
        list_of_days = []
        list_of_prices = []
        list_of_venues = []
        list_of_times = []
        list_of_pages = []
        list_of_prices = []
        pages = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button/p')
        for page in pages:
            list_of_pages.append(page)
        for i in range(len(list_of_pages)):
            if list_of_pages[i].text == "Show More":
                click_page = list_of_pages[i].find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button')
                driver.execute_script('arguments[0].scrollIntoView();', click_page)
                driver.execute_script('arguments[0].click();', click_page)
            
        artists = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div/div/div/a/div/div[2]/p[1]')
        date = date
        days = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div/div/a/div/div[1]/div/p')
        times = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div/div/a/div/div[1]/div/p')
        venues = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div/div/a/div/div[2]/div/p')
        prices = []
        for artist in artists:
            list_of_artists.append(artist)
        for day in days:
            list_of_days.append(day)
        for venue in venues:
            list_of_venues.append(venue)
        for time in times:
            list_of_times.append(time)
        
        for i in range(len(artists)):
            tickets_dict.append({'artist':list_of_artists[i].text,'date':date,'venue':list_of_venues[i].text,'city':city,'time':list_of_times[i].text,'day':list_of_days[i].text, 'price':list_of_ticket_prices[i],'ticket_type':list_of_ticket_types[i]})
        
        return tickets_dict
        print(tickets_dict)
    
        driver.quit()
        

    list_of_ticket_types = []
    list_of_ticket_prices = []
    def webdriver_ticket_prices(state, city, date):
        chromedriver_autoinstaller.install() 
        # Create Chromeoptions instance 
        options = webdriver.ChromeOptions() 
        service = Service()
        # Adding argument to disable the AutomationControlled flag 
        options.add_argument("--disable-blink-features=AutomationControlled") 
        # Exclude the collection of enable-automation switches 
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        # Turn-off userAutomationExtension 
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument('user-agent='+agent_random())
        # Setting the driver path and requesting a page 
        current_urls = [] 
        list_of_pages1 = []
        proxy2 = rand_proxy()
        options.add_argument(f'--proxy-server={proxy2}')
        driver = webdriver.Chrome(options=options, service=service)
        driver.get('https://www.vividseats.com/region/usa/'+state+'/'+city+'-tickets/40/concerts?startDate='+date+'&endDate='+date+'/')
        time.sleep(random.uniform(3,6))
        pages1 = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button/p')  
        for page1 in pages1:
            list_of_pages1.append(page1)
        for page2 in range(len(list_of_pages1)):
            if list_of_pages1[page2].text == "Show More":
                element_1 = list_of_pages1[page2].find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button')
                driver.execute_script('arguments[0].scrollIntoView();', element_1)
                time.sleep(random.uniform(3.5,6))
                driver.execute_script('arguments[0].click();', element_1)
                time.sleep(random.uniform(3.5,6))
        concert_counts = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div/div/a/div/div[3]/button')
        print(len(concert_counts))
        urls_dict = {}
        for concert in range(len(concert_counts)): 
            if concert >= 10:
                concert = concert+1
            current_url = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div['+str(concert+1)+']/div/a').get_attribute('href')
            
#             current_url = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div['+str(concert+1)+']/div/a/div/div[3]/button')
            urls_dict.update({concert:current_url})
        print(urls_dict)

        for url in urls_dict.values():
            print(url)
            chrome_options = webdriver.ChromeOptions()
            service = Service()
            chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
            # Exclude the collection of enable-automation switches 
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
            # Turn-off userAutomationExtension 
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_argument('user-agent='+agent_random())
            proxy4 = rand_proxy()
            chrome_options.add_argument(f'--proxy-server={proxy4}')
            driver = webdriver.Chrome(options=chrome_options, service=service)
            driver.get(url)
            time.sleep(random.uniform(4,6))
            try:
                captcha = driver.find_element(by.XPATH, "//*[@id='px-captcha']")
                print('captcha ='+str(captcha.text))
                action = ActionChains(driver)
                action.click_and_hold(on_element = captcha)
                action.perform()
                time.sleep(10)
                action.release(on_element = captcha)
                action.perform()
                time.sleep(0.5)
                action.release(on_element = captcha)
                time.sleep(random.uniform(3,5))
            except:
                print('No Captcha')
            
            try:
                concert_price = driver.find_element(By.XPATH, '//*[@id="content"]/div[6]/div[1]/div[2]/div[3]/div[1]/div/div[1]/div/span[1]').text
                ticket_type = driver.find_element(By.XPATH, '//*[@id="content"]/div[6]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div[1]/p').text
            except:
                concert_price = 'Unavailable'
                ticket_type = "Unavailable"
            
            list_of_ticket_prices.append(concert_price)
            list_of_ticket_types.append(ticket_type)
            driver.quit()
        
    def vividSeats(state, city, date):
        list_of_ticket_types = []
        list_of_ticket_prices = []
        tickets_dict = []
        webdriver_ticket_prices(state, city, date)
        Data = webdriver_tickets2(state, city, date)
        df1 = pd.DataFrame(data = Data)
        times = []
        days = []
        prices = []
        venues = []
        parking = []
        for i in df1['time']:
            i = str.replace(i[6:], '', '')
            times.append(i)
        for k in df1['day']:
            k = str.replace(k[:3], '', '')
            days.append(k)
        for n in df1['venue']:
            n = n.split('-')[0]
            venues.append(n)
        df1['price'] = df1['price'].str.extract('(\d+)')
        df1['time'] = times
        df1['day'] = days
        for l in df1['artist']:
            if "Parking" in l:
                parking.append('Parking')
            else:
                parking.append('Concert')
        df1['parking'] = parking
        
        df1.drop(df1[df1['parking']=="Parking"].index, inplace = True)
        df1.drop(['parking'], axis=1, inplace=True)
        print(df1)
        db = client['ConcertTickets']
        collection = db['VividSeats']
        print(collection)
        df1.reset_index(inplace = True)
        data_dict = df1.to_dict('records')
        print(data_dict)
        collection.insert_many(data_dict)


# In[238]:


vividSeats('co','denver','2023-08-08')


# In[ ]:





# In[ ]:





# In[ ]:




