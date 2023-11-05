

# Android environment
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.ios import XCUITestOptions
from time import sleep



tiktok_app_path = "/Users/hado/workspace/fossil/PythonForTester/app/Fossil_Global-Release-30409.apk"

appium_port = 'http://localhost:4723/'
iOS_path = "wd/hub"

like_button = '//android.widget.Button[@content-desc="Like video. 0 likes"]'




def test_open_app():
    options = UiAutomator2Options()
    # options.platform_version = "13"
    # options.uuid = "emulator-5554"
    #options.app = "/Users/147230/Documents/Somtudy/PythonForTester/app/Fossil_Global-Release-30409.apk"
    options.app_package = "com.google.android.calculator"
    options.app_activity = "com.android.calculator2.Calculator"
    options.no_reset = True
    
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options= options)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="1").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="plus").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="2").click()
    result = driver.find_element(by=AppiumBy.ID,value="result_preview").text
    assert result == "3"

def test_ios_calendar():
    options = XCUITestOptions()
    options.bundle_id = "com.apple.mobilecal"
    options.platform_version = "16.2"
    options.platform_name = "iOS"
    options.device_name = "iphone 14"
    driver = webdriver.Remote('http://localhost:4723', options= options)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Thêm").click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Title").send_keys("Event 1")
    

def open_Android_tiktok():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "sdk_gphone64_arm64"
    options.platform_version = "14"
    options.app = tiktok_app_path
    options.no_reset = True
    # driver = webdriver.Remote(appium_port, options =options)

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

    driver = webdriver.Remote("http://127.0.0.1:4723/", caps)




    sleep(15)
    driver.find_element(by=AppiumBy.XPATH,value = like_button).click()

open_Android_tiktok()    

# test_ios_calendar()