# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:31:20 2021

@author: lordm
"""


import numpy as np
import pandas as pd

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from webscraper_helper import get_table


# Path ha to be "C:\Users\lordm\Desktop\Uni\SE_PR_in_AI\Code\webscraping"

"""
Scrap Mock Draft Data from fantasyfootballcalculator.com
- 12-Team, PPR
- years: 2021 to 2015
- load all Mock drafts in 14 days prior to first game of season
- only drafts with >= 6 humans and 15 finished rounds
"""


webpath_base = 'https://fantasyfootballcalculator.com/mock-draft/results/format/'
webpath_base += 'ppr/teams/12?page='
date_dict = {2021: '10/09/2021', 
             2020: '11/09/2020', 2019: '06/09/2020', 2018: '07/09/2020', 
             2017: '08/09/2020', 2016: '09/09/2020', 2015: '11/09/2020'}

#changing chromedriver default options
options = Options()
options.headless = False
#options.add_argument('window-size=2400x1080') 

page_nr = '25'
webpage = webpath_base + page_nr

#execute chromedriver with edited options
driver = webdriver.Chrome('.\chromedriver.exe')
driver.get(webpage)
driver.maximize_window()
time.sleep(5) # Let the user actually see something!

# accept Cookies
#accept = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_evidon-accept-button"]')))
#accept.click()

html = driver.page_source
df = get_table(html)

# Next: click with the driver the mock draft and load in a nested list/numpy








driver.quit()






