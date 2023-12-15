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
time.sleep(3)

# 切换手机号登录
element = chrome.find_element(by=By.XPATH, value=r'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div/span')
element.click()

# 输入电话号码
element = chrome.find_element(by=By.NAME, value="mobile_input")
element.send_keys(user)

# 勾选协议
element = chrome.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/label/span[1]/input')
element.click()

# 点击下一步
element = chrome.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/button')
element.click()

# 点击密码框，并输入
time.sleep(3)
element =chrome.find_element(by=By.NAME, value='password_input')
element.send_keys(passwd)

# 点击下一步（登录）
element = chrome.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[3]/div/button')
element.click()
time.sleep(3)

# 点击菜单
element = chrome.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[2]/div/div/div/div/div[7]/div')
element.click()
time.sleep(3)

# 点击消息
element = chrome.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div/div/div[1]/ul/li[1]/div/i')
element.click()

# 切换窗口
time.sleep(3)
windows = chrome.window_handles
chrome.switch_to.window(windows[-1])

# 点击通讯录
time.sleep(1)
element = chrome.find_element(by=By.XPATH, value='//*[@id="app"]/section/div/section/section/section[5]/div')
element.click()

# 点击外部联系人
time.sleep(3)
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-contacts"]/div/div[1]/div[4]/div')
element.click()

# 点击联系人
time.sleep(3)
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-contacts"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[2]')
element.click()
time.sleep(3)

# 点击弹窗中的信息按钮
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-userCardModal"]/div/div[1]/div/div/div/div[1]/div[1]/div[3]/div[3]/button[1]')
element.click()
time.sleep(1)

# 点击其他用户（BUG：跳转的页面上无输入框，需要先点击其他用户再点击回要发送消息的用户才会加载输入框）
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[1]/div[1]/div[1]/div[1]/div[4]/div/div[1]/div/div/div/div[2]/div[3]/div/div/div')
element.click()
time.sleep(1)

# 点击要发送信息的人
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[1]/div[1]/div[1]/div[1]/div[4]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div')
element.click()
time.sleep(1)

# 点击输入框
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div')
element.click()

# 输入信息，并发送
time.sleep(2)
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/pre/p/br')
time.sleep(1)
element.send_keys("你好，这是自动化测试消息！")
element = chrome.find_element(by=By.XPATH, value='//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/pre/p')
time.sleep(1)
element.send_keys(Keys.ENTER)

time.sleep(5)
# 关闭浏览器
chrome.close()

