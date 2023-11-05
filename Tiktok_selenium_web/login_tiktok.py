from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from time import sleep
from selenium.webdriver.support.ui import Select

import os
import linecache

target_url = "https://www.tiktok.com/explore"

login_header_button = "//button[@id='header-login-button']"

#button appear after click login
login_by_QR = "//a[@class='tiktok-t5chka-ALink epl6mg0'][1]"
login_by_phone_mail = "//a[@class='tiktok-t5chka-ALink epl6mg0'][2]"

#button appear after click login by phone mail
change_to_login_by_email = "//a[@href='/login/phone-or-email/email']"

input_email = ["//input[@placeholder='Email or username']","ddj54893@nezid.com"]
input_password = ["//input[@type='password']","12345678a@"]
login_button = "//button[@data-e2e='login-button']"

# User screen
upload_button = "//a[@aria-label='Upload a video']"

# Upload screen
select_upload_file = "//div[@class='jsx-2751257330 upload-card before-upload-stage']"
frame = "//iframe"
input_upload_file = "//input[@type='file']"
file_to_upload = "/Users/feed/Downloads/Snaptik.app_7197385203885853998.mp4"
copyright_toggle = "//input[@id='tux-4']"
post_button = "//button[@class='css-y1m958']"
manage_video_posted = "//div[@class='tiktok-modal__modal-button is-line']"

#content page
content_upload_button = "//button[@class='css-5qkbk']"



def set_up_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    # Prevent automation detected
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--profile-directory=Default")
    # options.add_argument("--user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)


    driver = webdriver.Chrome(options=options)

    # disable automation detection
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    # driver= webdriver.Chrome()
    driver.get(target_url)
    sleep(5)
    return driver

def quit_browser(driver):
    driver.quit()

def login_by_email(driver):

    driver.find_element(By.XPATH,value=login_header_button).click()
    sleep(1)
    driver.find_element(By.XPATH,value=login_by_phone_mail).click()
    sleep(1)
    driver.find_element(By.XPATH,value=change_to_login_by_email).click()
    sleep(1)
    driver.find_element(By.XPATH,value=input_email[0]).send_keys(input_email[1])
    # driver.find_element(By.XPATH,value=input_email[0]).send_keys("asdasd")    
    sleep(1)
    driver.find_element(By.XPATH,value=input_password[0]).send_keys(input_password[1])



    sleep(1)
    driver.find_element(By.XPATH,value=login_button).click()
    sleep(15)
    #Should manual verify image capcha before run next step

def upload_video(driver):

    driver.find_element(By.XPATH,value=upload_button).click()
    sleep(1)

    #Should change frame before find the upload element
    driver.switch_to.frame(driver.find_element(By.XPATH,value=frame))
    sleep(3)
    # input_upload_file directly without clicking to the select file OS
     # http://allselenium.info/file-upload-using-python-selenium-webdriver/
    driver.find_element(By.XPATH,value=input_upload_file).send_keys(file_to_upload)
    #When draged the file, the post title was automatically set by video name
    sleep(10)

    #toggle copyright_check and wait until it success verifying
    driver.find_element(By.XPATH,value=copyright_toggle).click()
    sleep(7)
    #now click to post the video
    driver.find_element(By.XPATH,value=post_button).click()
    sleep(10)
    #go back to home screen
    driver.find_element(By.XPATH,value=manage_video_posted).click()
    sleep(2)

    

def click_upload_in_content_page(driver):
    driver.find_element(By.XPATH,value=content_upload_button).click()
    sleep(2)

if __name__ == "__main__":
    driver = set_up_chrome()
    login_by_email(driver)    
    sleep(30)
    # upload_video(driver)
    quit_browser(driver)