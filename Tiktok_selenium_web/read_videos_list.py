from selenium import webdriver
from time import sleep
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
my_url = "https://www.tiktok.com/@feed6448/video/7274973518272482561"

login_dismiss_button = "//div[@aria-label='Close']"
next_video_el = "//button[@aria-label='Go to next video']"



def verify_capcha_image(driver):
    while True:
        try:
            target = driver.find_element(By.XPATH,"//div[@class='secsdk-captcha-drag-icon sc-kEYyzF fiQtnm']")

            action2 = ActionChains(driver)
            action2.drag_and_drop_by_offset(target,168,0)
            action2.perform()
            sleep(5)
        except selenium.common.exceptions.NoSuchElementException:
            print("Verification success")
            break
 
    
def go_to_my_page(driver):
    driver.find_element(By.XPATH,login_dismiss_button).click()
    sleep(5)
    driver.find_element(By.XPATH,"//span[contains(text(),'feed6448')]").click()
    sleep(10)

    my_video_list = driver.find_elements(By.XPATH,"//div[@class='tiktok-1jxhpnd-DivContainer e1yey0rl0']")
    my_video_list[0].click()
    sleep(30)

    return my_video_list

def view_all_my_videos(driver):
    for i in range(len(go_to_my_page(driver))):
        driver.find_element(By.XPATH,next_video_el).click()
        sleep(15)


def close_browser(driver):
    driver.quit()

def open_tiktok():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(options)
    driver.get(my_url)  
    sleep(20)
    # verify_capcha_image(driver)
    # sleep(2)
    view_all_my_videos(driver)
    sleep(2)
    close_browser(driver)

open_tiktok()