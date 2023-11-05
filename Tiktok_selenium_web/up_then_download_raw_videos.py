from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
import linecache


target_url = "https://snaptik.app/vn#google_vignette"

marked_video_list = []
#homes page
link_input_to = "//input[@name='url']"
download_button = "//button[@type='submit']"

#download page
download_button_as_noAd = "//a[@class='button download-file mt-3']"
#download another video
goback_to_mainscreen = "//a[@class='button is-black mt-3']"

cwd = os.getcwd()

def read_file(line_number):
    # f = open(cwd+"/videos.txt", "r")
    # print(f.readline())
    # f.close()    
    x = linecache.getline(cwd+"/videos.txt",line_number)
    print(x)
    return x

def set_up_chrome():
    driver = webdriver.Chrome()
    driver.get(target_url)
    sleep(5)
    return driver

def input_file_in_home_page(driver,line_number):

    url = driver.find_element(By.XPATH,value=link_input_to)
    # url.click()
    url.send_keys(read_file(line_number))
    sleep(3)
    # driver.find_element(By.XPATH,value=download_button).click()
    # sleep(1)

def click_download_noAd(driver):

    driver.find_element(By.XPATH,value=download_button_as_noAd).click()
    sleep(1)
    driver.find_element(By.XPATH,value=goback_to_mainscreen).click()

def check_file_has_downloaded(line_number):
    text = read_file(line_number)
    x = text.index("video/") # get the "video/" index location, then get the video id 
    print(x)
    print(text[x:-1]) # the video id path will display here
    video_id = text[(x+6):-1] # add 6 index to remove "video/" part
    print("Video id =",video_id)

    # Snaptik.app_7192882443400056106.mp4
    snaptik_file_header = "Snaptik.app_"
    snaptik_file_footer = ".mp4"
    print(snaptik_file_header+video_id+snaptik_file_footer)

    if os.path.isfile("/Users/feed/Downloads/"+snaptik_file_header+video_id+snaptik_file_footer):
        print("File download is completed")
    else:
        print("No file found")
        raise(AssertionError)

def quit_browser(driver):
    driver.quit()

if __name__ == "__main__":
    chrome = set_up_chrome()
    input_file_in_home_page(chrome,3) # select line number 2 in the videos.txt file
    click_download_noAd(chrome)
    check_file_has_downloaded(3) # check line number 2 in the videos.txt file
    quit_browser(chrome)

