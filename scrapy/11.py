import time
from requests import Session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
chrome = webdriver.Chrome()
session = Session()
url = 'https://seer.61.com/events/2023return/'
chrome.get(url)

try:

    accountSwitch = chrome.find_element(By.CLASS_NAME, "head__btn-login").find_element(By.CLASS_NAME,
                                                                                       "head__btn")
    accountSwitch.click()

    time.sleep(2)


    print('find it!')

    time.sleep(2)
    print('代码运行到这里了')
    chrome.implicitly_wait(10)
    wait = WebDriverWait(chrome, 5)
    js = "https://webres.61.com/2023/seer.61.com/202309return/js/index.js?20230926123912"
    chrome.get(js)
    print()
    for Clss in chrome.find_elements(By.TAG_NAME,'span'):
        print(Clss.text)
    taomee = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "other-ways__taomee")))

    #     taomee = chrome.find_elements(By.CLASS_NAME, "other-ways__taomee")
    # print(len(taomee))
    #taomee.click()
    print("找到淘米登录方式！")

    checkBox = chrome.find_element(((By.CLASS_NAME, 'icon__checkbox'))).click()

except:
    print("没找到这个元素")
    # print(chrome.page_source)
def f(a,b):
    return a,b
