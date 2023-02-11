#Finnegan Damore Johann @ Feb 9 2023

#Contentful file uploader



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pathlib import Path

import time

import os, fnmatch
import sys


#sys path of executable
print(sys.argv)
filterPath = Path(os.path.dirname(sys.argv[0]) + '/upload')
print(filterPath)


class UploadFiles():

    webPage = "https://app.contentful.com"
    driver = None
    tagNamesInOrder = []
    uploadTags = None


    def connect(self):

        self.driver = webdriver.Chrome(Path('./driver/chromedriver.exe'))
        self.driver.get(self.webPage)
        self.driver.implicitly_wait(10)


    def get_user_input(self):
        input('enter any button and press enter to continue to upload data to this page')
        return True


    def click_to_open_upload_dropdown(self):

        buttons = self.driver.find_elements(by=By.CLASS_NAME, value='css-ndrb9n')

        for button in buttons:
            button.click()

        time.sleep(4)


    def retrieve_tags(self):

        classTags = self.driver.find_elements(by=By.CLASS_NAME, value="css-imt9h5")

        for p in classTags:
            self.tagNamesInOrder.append(p.text)

        print(self.tagNamesInOrder)

    def retrieve_upload_tags(self):

        self.uploadTags = self.driver.find_elements(by=By.ID, value="fsp-fileUpload")
        print(self.uploadTags)

    def upload(self):
        print('uploading images')
        i = 0
        print('upload tags are ' + str(self.uploadTags) )
        for i in range(0, len(self.uploadTags)):
            images = fnmatch.filter(os.listdir(filterPath), f'{self.tagNamesInOrder[i]}*')
            if str(self.tagNamesInOrder[i]) == 'en-IE':
                 images = images + fnmatch.filter(os.listdir(filterPath), 'xx-XX*')
            print(images)
            if len(images) > 0:
                image = images[0]
                print(f'uploading image : {filterPath}/{image} ')
                self.uploadTags[i].send_keys(f'{filterPath}/{image}')
            i += 1

        print('uploaded')


t = UploadFiles()

t.connect()

while t.get_user_input():

    t.click_to_open_upload_dropdown()

    t.retrieve_tags()

    t.retrieve_upload_tags()

    t.upload()

