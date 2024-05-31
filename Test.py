from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from User_Agent import User_Agent

import pandas as pd
import time
import urllib.request
import bs4



# Firefox Options
option = FirefoxOptions()
# option.add_argument("--headless")
option.set_preference("general.useragent.override", User_Agent())
option.add_argument("--disable-gpu")
option.add_argument("--disable-software-rasterizer")
option.add_argument('--ignore-certificate-errors')
option.add_argument('--allow-running-insecure-content')
option.add_argument("--mute-audio")
option.add_argument("--window-size=1920,1080")


def videoDownload(video_url, CreatorName, Number):
    try:
        print('Download...')
        urllib.request.urlretrieve(video_url, CreatorName + '_' + str(Number) + '.mp4')
        print(CreatorName + '_' + str(Number) + '.mp4' + ' Download Success')
    except:
        print('Download Error')
    return 'OK'

# Driver Create
print("Start")
driver = webdriver.Edge(options=option)
CreatorName = 'wdz_pet'
driver.get("https://www.tiktok.com/@" + CreatorName)
time.sleep(5)
x = input()
for i in range(1, 375):
    try:
        all_handles = driver.window_handles

        driver.switch_to.window(all_handles[0])
        driver.execute_script("window.scrollTo(0,38759)")
        time.sleep(3)

        Click_Video_Url = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div[2]/div/div[2]/div[2]/div/div[' + str(i) + ']/div[1]/div/div/a').get_property('href')
        time.sleep(2)

        driver.switch_to.window(all_handles[1])
        driver.get(Click_Video_Url)
        time.sleep(5)

        x = driver.current_url[38: 57]
        url = driver.find_element(By.XPATH, '//*[@id="xgwrapper-4-'+ str(x) +'"]/video').get_property('src')
        time.sleep(2)





        videoDownload(url, CreatorName, i)
        time.sleep(2)
    except:
        print('Error')

driver.close()

