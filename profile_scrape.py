from typing import Awaitable
from selenium import webdriver
from driver_location import *
from selenium.webdriver.common.by import By
from Functions.convert_value import *
import numpy as np
import time

class Profile():

    def __init__(self,username,n) -> None:
        self.videos = []
        self.username = username
        self.profile_page_url = "https://www.tiktok.com/@" + self.username
        self.driver = webdriver.Chrome(ChromeDriver_Location)
        self.driver.get(self.profile_page_url)

        followers = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong')
        self.followers = convert_value(followers.text)

        for i in range(1,n+1):
            #XPATH for vidoes on a profile page
            try:
                video = self.driver.find_element(By.XPATH,f'//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div/div[{i}]/div[1]/div/div/a')
                url = video.get_attribute('href')
                self.videos.append(url)
            except:
                self.videos = self.videos

    def get_information(self):

        self.likes = []
        self.comments = []
        self.shares = []
        self.duration = []

        for i in self.videos:
            #likes
            self.driver.get(i)
            try:
                like_element = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[3]/button[1]/strong')
                likes = like_element.text
                self.likes.append(convert_value(likes))
            

            #comments
            
                comment_element = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[3]/button[2]/strong')
                comments = comment_element.text
                self.comments.append(convert_value(comments))
    
            
            #shares 
        
                share_element = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[3]/button[3]/strong')
                shares = share_element.text
                self.shares.append(convert_value(shares))

            #duration
                duration_element = self.driver.find_element(By.CSS_SELECTOR,'div.tiktok-1g3unbt-DivSeekBarTimeContainer.e123m2eu1')
                time.sleep(0.25)
                duration = duration_element.get_attribute('innerHTML')
                self.duration.append(convert_time(duration))
                
            
            except:
                self.likes = self.likes 
                self.comments = self.comments
                self.shares = self.shares
                self.duration = self.duration

    def quit(self):
        self.driver.quit()



profile1 = Profile("addisonre",5)
profile1.get_information()
profile1.quit()