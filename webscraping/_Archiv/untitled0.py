# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:50:26 2021

@author: lordm
"""

#https://medium.com/@shivangisareen/for-anyone-using-jupyter-notebook-installing-packages-18a9468d0c1c

#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# import libraries
import subprocess
import pandas as pd
import pickle

import Scrappers
from tipico import scrap_tipico
df_tipico = scrap_tipico()

#############################

#changing chromedriver default options
options = Options()
options.headless = False
#options.add_argument('window-size=2400x1080') 

web = 'https://sports.tipico.de/en/live/' 
#execute chromedriver with edited options
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get(web)
driver.maximize_window()

# accept Cookies
accept = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_evidon-accept-button"]')))
accept.click()

# Breaking down the code:
# options = Options() creates an instance of the Options class
# options.headless = True turns on the headless mode
# options.add_argument(‘window-size=1920x1080’) opens the windows in a customized size on the background
# webdriver.Chrome(path, options = options) applies the changes we made in the chromedriver
# driver.get opens the browser
# web represents the betting site’s URL, while path represents the chromedriver’s path in your computer
# If you don’t want to work in headless mode, then write option.headless=False and use driver.maximize_window() instead of options.add_argument(‘window-size=1920x1080’) as shown in the full code.
# Select('...') selects dropdown menus
# first_dropdown one of the three dropdowns that contain betting markets
# first_dropdown.select_by_visible_text() selects an element inside the dropdown menu with the help of the betting market’s name.




#Initialize your storage
teams = []
x12 = []
over_under = []
btts = []
odds_events = []

#select values from dropdown
first_dropdown = Select(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/main/section/div/div/div[4]/div[1]/div/div[1]/select[1]'))))
first_dropdown.select_by_visible_text('3-Way')


#Looking for live events 'Program_LIVE'
box = driver.find_element_by_xpath('//div[contains(@testid, "Program_LIVE")]')
#Looking for 'sports titles'
sport_title = box.find_elements_by_class_name('SportTitle-styles-sport')
