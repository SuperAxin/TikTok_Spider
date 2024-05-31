
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from User_Agent import User_Agent

class Catch:
    def __init__(self, Creator):
        self.Creator = Creator

    def FireFox(self):
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

        # 啟動Driver
        print('Start FireFox Driver')
        self.driver = webdriver.Edge(options=option)
        self.driver.get("https://www.tiktok.com/@" + self.Creator)
        _ = input('手動機器人驗證...完成後按下 Enter 繼續')

    def VideoDownload(self):

        # 點擊第一個影片
        Click_Video_Url = self.driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/a').get_property('href')
        time.sleep(2)

        self.driver.get(Click_Video_Url)
        time.sleep(2)

        # 進入到影片網址
        Video_url = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/video').get_property('src')
        print(Video_url)
        self.driver.get(Video_url)
        time.sleep(2)

        # 擷取Cookies 並將 cookies 轉換為 requests 可接受的格式
        cookies = self.driver.get_cookies()
        cookies_dict = {}
        for cookie in cookies:
            cookies_dict[cookie['name']] = cookie['value']

        # 使用 requests 發送帶有 cookies 的請求
        response = requests.get(self.driver.current_url, cookies=cookies_dict)
        if response.status_code == 200:
            # 將 response 中的內容保存為影片
            with open('video.mp4', 'wb') as f:
                f.write(response.content)
            print("影片下載完成")
        else:
            print("無法下載影片，狀態碼：", response.status_code)

        _ = input('Press Enter to Close...')

        #　關閉瀏覽器
        self.driver.close()


