from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.chrome.options
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

target_url = "https://www.tiktok.com/search/video?q=dog%20meme"

videos_path = "//div[@class=' tiktok-1as5cen-DivWrapper e1cg0wnj1']/a"
#this element maybe changed by tiktok, for that the video list may get blank 
# => should re-capture the element again

video_data = []
cwd = os.getcwd()

def open_tiktok_web():
    print ("haha")
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    
    driver = webdriver.Chrome(options=options)
    driver.get(target_url)
    time.sleep(15)
    return driver

if __name__ == "__main__":
    driver = open_tiktok_web()
    # driver = webdriver.Firefox()

    #before get the list, you should manual pass the verify image sessioh
    video_list = driver.find_elements(By.XPATH,videos_path)
    for i in video_list:
        print(i.get_attribute('href'))
        video_data.append(i.get_attribute('href'))
    time.sleep(10)
    print(video_data)

    file = open(cwd+'/videos.txt','w')
    for i in video_data:
        file.write(i+"\n")
    file.close()
    driver.close()


