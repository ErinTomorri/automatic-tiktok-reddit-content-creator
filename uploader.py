from distutils.command.upload import upload
from click import option
import undetected_chromedriver as uc
import requests
import asyncio
import glob, os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui

path = "C:/Program Files (x86)/chromedriver.exe"
list1 = []
path1 = "C:/Users/etomo/OneDrive/Desktop/tiktok-askreddit-main/render/"
async def main():

    options = uc.ChromeOptions()

    options.add_argument("--log-level=3")
    options.add_argument('disable-infobars')

    driver = uc.Chrome(options=options)
    driver.get("https://www.tiktok.com/login")

    driver.set_page_load_timeout(25)
    driver.set_window_size(1920, 1080)

    os.chdir("C:/Users/etomo/OneDrive/Desktop/tiktok-askreddit-main/render")
    for file in glob.glob("*.mp4"):
        list1.append(file)

    print(list1)
    num = 0

    #for num in range(len(list1)):
    if num == 0:
        user1 = "user"
        pass1 = "pass"

        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[2]').click()
        time.sleep(5)
        
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[1]/a').click()
        time.sleep(5)

        username = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input')
        username.click()
        username.send_keys(user1)
        time.sleep(5)

        password = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input')
        password.click()
        password.send_keys(pass1)

        log = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button')
        log.click()

        time.sleep(5)

        log = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button')
        log.click()

        time.sleep(5)
        
        upload0 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/a/span/svg/path')
        upload0.click()
        time.sleep(5)

        upload1 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button/div/div')
        upload1.click()

        video = path1+list1[num]
        pyautogui.write(video, interval=0.25)
        


if __name__ == '__main__':
    [os.mkdir(dir) for dir in ['output','render','backgrounds'] if not os.path.exists(dir)]
    asyncio.run(main())
