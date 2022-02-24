from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import threading

options = Options()
options.add_argument('--disable-notifications')

PATH = "D:\ChromeDriver_Python\chromedriver.exe"   #Path to chromedriver application
driver = webdriver.Chrome(PATH, options=options)   #Opens chromedriver and disable notification

driver.get("https://www.subpals.com/login/final/<Channel ID Here>/")  #Your Channel Id, remove '< >'
password = driver.find_element_by_xpath('//*[@id="core-wrapper"]/section/div/div/div/div/div/form/div[2]/input')
password.send_keys('<Password Here>')         #Your Password

letme = driver.find_element_by_xpath('//*[@id="core-wrapper"]/section/div/div/div/div/div/form/button')
letme.click()
time.sleep(1.5)

#Check whether page is active to be used
try:
    activate = driver.find_element_by_xpath('//*[@id="core-wrapper"]/section/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/a')
    activate.click()
    time.sleep(1)
except Exception:
    try:
        driver.find_element_by_xpath('//*[@id="core-wrapper"]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[5]/a')
    except Exception:
        driver.quit()

while True:
    # skip Button
    try:
        skip = driver.find_element_by_xpath('//*[@id="core-wrapper"]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[5]/a')
    except Exception:
        break
    # Select the like and subscribe button
    skip.send_keys(Keys.SHIFT, Keys.TAB, Keys.TAB, Keys.ENTER)
    time.sleep(1.5)

    # Switch control to youtube window
    try:
        chwnd = driver.window_handles[1]
        driver.switch_to.window(chwnd)
    except Exception:    #When page is stuck
        driver.refresh()
        time.sleep(1.5)
        continue

    def c():
        # Closes youtube window
        driver.close()

    def t():
        # Switch to main window
        ptwnd = driver.window_handles[0]
        driver.switch_to.window(ptwnd)
        time.sleep(30)      #Timer for confirm button to turn green
        # Click Confirm Button
        skip.send_keys(Keys.SHIFT, Keys.TAB, Keys.ENTER)

    t1 = threading.Thread(target=t)
    t2 = threading.Thread(target=c)
    t2.start()
    t2.join()
    t1.start()
    t1.join()
    time.sleep(27)    #Timer for next page to appear

time.sleep(5)
driver.quit()
