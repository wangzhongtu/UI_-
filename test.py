import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = os.path.abspath(r"./chrome_driver/chrome-win64/chome.exe")
chrome = webdriver.Chrome()

chrome.get("http:feishu.cn/")
chrome.maximize_window()

time.sleep(3)

user = "17512058948"
passwd = "gkhn95324ltu"

# 关闭弹窗
try:
    element = chrome.find_element(by=By.XPATH, value=r'/html/body/div[2]/div[2]/div/div/div')
    element.click()
except Exception as e:
    pass

# 点击登录按钮
element = chrome.find_element(by=By.XPATH, value=r'//*[@id="app"]/div/div[2]/div/div/div/div/a[3]')
element.click()

time.sleep(5)
element = chrome.find_element(by=By.XPATH, value=r'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div/span')
element.click()


element = chrome.find_element(by=By.NAME, value="mobile_input")
element.send_keys(user)

element = chrome.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/label/span[1]/input')
element.click()

element = chrome.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/button')
element.click()

time.sleep(3)
element =chrome.find_element(by=By.NAME, value='password_input')
element.send_keys(passwd)

element = chrome.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[3]/div/button')
element.click()
time.sleep(5)

# 点击网页版
element = chrome.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/a[2]')
element.click()

# 切换窗口
time.sleep(3)
windows = chrome.window_handles
chrome.switch_to.window(windows[-1])

# 点击用户
time.sleep(1)
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[1]/div[1]/div[1]/div[1]/div[4]/div/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/p')
element.click()
time.sleep(1)

element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div')
element.click()

#点击输入框,并发送

element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/pre/p/br')
# element.click()
time.sleep(1)
element.send_keys("你好，这是自动化测试消息！")
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/pre/p')
time.sleep(1)
element.send_keys(Keys.ENTER)

time.sleep(5)
chrome.close()