
from selenium import webdriver
from driver_location import *
from selenium.webdriver.common.by import By
from Functions.convert_value import *
import numpy as np
import time

class Search():

    def __init__(self,tag,num_profiles) -> None:
        self.usernames = []
        self.tag = tag
        self.tag_page_url = "https://www.tiktok.com/tag/" + tag
        self.driver = webdriver.Chrome(ChromeDriver_Location)
        self.driver.get(self.tag_page_url)

        for i in range(1,num_profiles+1):
            try:
                time.sleep(0.05)
                username_element = self.driver.find_element(By.XPATH,f'//*[@id="app"]/div[2]/div[2]/div/div[2]/div/div[{i}]/div[1]/div/div/a/div/div[2]/a[2]/p/h4')
                self.usernames.append(username_element.text)
            except:
                self.usernames = self.usernames

        self.driver.quit()


