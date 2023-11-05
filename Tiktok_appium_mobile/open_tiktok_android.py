
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


from time import sleep


heart_icon = '//android.widget.ImageView[@content-desc="Like"]'


caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "14"
caps["appium:deviceName"] = "sdk_gphone64_arm64"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:app"] = "/Users/feed/Downloads/TikTok_31.1.4_apkcombo.com.apk"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True


def open_mobile_app():
    driver = webdriver.Remote("http://127.0.0.1:4723", caps)
    sleep(5)
    return driver


def press_like_post(driver):
    press_heart_button = driver.find_element(by=AppiumBy.XPATH,value=heart_icon)
    spam_like_button = driver.find_element(by=AppiumBy.ID,value="com.zhiliaoapp.musically:id/lfb")
    spam_like_button_2 = driver.find_element(by=AppiumBy.ID,value="com.zhiliaoapp.musically:id/eiv")
    press_heart_button.click()

# spam like functions
def spam_like_in_live(driver):
    for i in range (1,3600):
        driver.execute_script("mobile: doubleClickGesture", {'x':529,'y':1108})
        sleep(5)

if __name__ == '__main__':
    #start appium server     appium  --allow-cors | npx kill-port 4723
    #before run this case, should manual open the live screen
    spam_like_in_live(open_mobile_app())