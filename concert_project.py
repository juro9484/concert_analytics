#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

response = requests.get(
    "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=100",
    headers={"Authorization": "dpmqaazul1il0snzb31sgyric9plmfbuezeuth32"}
)
 
# response.json()
array_of_proxies = []
# response.json()
for i in response.json()['results']:
#     if i['country_code'] == 'US':
        array_of_proxies.append(str(i['proxy_address'])+":"+str(i['port']))

def rand_proxy():
    proxy = random.choice(array_of_proxies)
    return proxy

tickets_dict = []




# In[ ]:


def webdriver_tickets(event, content):
    response = requests.get(
    "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=100",
    headers={"Authorization": "dpmqaazul1il0snzb31sgyric9plmfbuezeuth32"}
    )
    print(requests.json())
    array_of_proxies = []
    # response.json()
    for i in response.json()['results']:
    #     if i['country_code'] == 'US':
            array_of_proxies.append(str(i['proxy_address'])+":"+str(i['port']))

    def rand_proxy():
        proxy = random.choice(array_of_proxies)
        return proxy

    tickets_dict = []
    def webdriver_tickets2(state, city, date):
        chromedriver_autoinstaller.install() 
        # Create Chromeoptions instance 
        options = webdriver.ChromeOptions() 
        # Adding argument to disable the AutomationControlled flag 
        options.add_argument("--disable-blink-features=AutomationControlled") 
        # Exclude the collection of enable-automation switches 
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        # Turn-off userAutomationExtension 
        options.add_experimental_option("useAutomationExtension", False) 
        # Setting the driver path and requesting a page 
        proxy = rand_proxy()
        # options.add_argument(f'--proxy-server={proxy}')
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
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
        
        for i in range(len(list_of_artists)):
            tickets_dict.append({'artist':artists[i].text,'date':date,'venue':list_of_venues[i].text,'city':city,'time':list_of_times[i].text,'day':list_of_days[i].text})
    
        return tickets_dict
    
    driver.quit()


# In[ ]:


def webdriver_ticket_prices(state, city, date):
    chromedriver_autoinstaller.install() 
    # Create Chromeoptions instance 
    options = webdriver.ChromeOptions() 
    # Adding argument to disable the AutomationControlled flag 
    options.add_argument("--disable-blink-features=AutomationControlled") 
    # Exclude the collection of enable-automation switches 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    # Turn-off userAutomationExtension 
    options.add_experimental_option("useAutomationExtension", False) 
    # Setting the driver path and requesting a page 
    current_urls = [] 
    list_of_pages1 = []
    proxy2 = rand_proxy()
    options.add_argument(f'--proxy-server={proxy2}')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get('https://www.vividseats.com/region/usa/'+state+'/'+city+'-tickets/40/concerts?startDate='+date+'&endDate='+date+'/')
    time.sleep(3.5)
    pages1 = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button/p')  
    for page1 in pages1:
        list_of_pages1.append(page1)
    for page2 in range(len(list_of_pages1)):
        if list_of_pages1[page2].text == "Show More":
            element_1 = list_of_pages1[page2].find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button')
            driver.execute_script('arguments[0].scrollIntoView();', element_1)
            time.sleep(random.uniform(3,5))
            driver.execute_script('arguments[0].click();', element_1)
            time.sleep(random.uniform(3,5))
    concert_counts = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div/div/a/div/div[3]/button')
    print(len(concert_counts))
    for concert in range(len(concert_counts)): 
        if concert >= 10:
            concert = concert+1
        chrome_options = webdriver.ChromeOptions()
        proxy3 = rand_proxy()
        chrome_options.add_argument(f'--proxy-server={proxy3}')
        driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        driver.get('https://www.vividseats.com/region/usa/'+state+'/'+city+'-tickets/40/concerts?startDate='+date+'&endDate='+date+'/')
        time.sleep(3.5)
        pages3 = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button/p')
        for page3 in range(len(pages3)):
            if pages3[page3].text == "Show More":
                element_2 = pages3[page3].find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div[12]/button')
                driver.execute_script('arguments[0].scrollIntoView();', element_2)
                time.sleep(random.uniform(1,3))
                driver.execute_script('arguments[0].click();', element_2)
                time.sleep(random.uniform(1,3))
        element_3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[5]/div[2]/div['+str(concert+1)+']/div/a/div/div[3]/button')
        driver.execute_script("arguments[0].scrollIntoView();", element_3)
        time.sleep(random.uniform(3,5))
        driver.execute_script("arguments[0].click();", element_3)
        time.sleep(random.uniform(3,5))
        current_urls.append(driver.current_url)
        print(driver.current_url)
        driver.quit()
        
    for url in current_urls:
#         chrome_options = webdriver.ChromeOptions()
#         proxy4 = rand_proxy()
#         chrome_options.add_argument(f'--proxy-server={proxy4}')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(5.5)
        try:
            concert_price = driver.find_element(By.XPATH, '//*[@id="content"]/div[6]/div[1]/div[2]/div[3]/div[1]/div/div[1]/div/span[1]').text
            ticket_type = driver.find_element(By.XPATH, '//*[@id="content"]/div[6]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div[1]/p').text
        except:
            concert_price = 'Unavailable'
            ticket_type = "Unavailable"
            
        list_of_ticket_prices.append(concert_price)
        list_of_ticket_types.append(ticket_type)
        driver.quit()
        


# In[ ]:


def vividSeats(state, city, date):
    tickets_dict = []
    list_of_ticket_types = []
    list_of_ticket_prices = []
    webdriver_ticket_prices(state, city, date)
    webdriver_tickets(state, city, date)
    df1 = pd.DataFrame(data = tickets_dict)
    print(df1)
    times = []
    days = []
    prices = []
    for i in df1['time']:
        i = str.replace(i[6:], '', '')
        times.append(i)
    for k in df1['day']:
        k = str.replace(k[:3], '', '')
        days.append(k)
    df1['price'] = df1['price'].str.extract('(\d+)')
    for x in df1['price']:
        x = int(x)
        prices.append(x)
    df1['time'] = times
    df1['day'] = days
    df1['price'] = prices
    db = client['ConcertTickets']
    collection = db['VividSeats']
    df1.reset_index(inplace = True)
    data_dict = df1.to_dict('records')
    print(data)
    # collection.insert_many(data_dict)

