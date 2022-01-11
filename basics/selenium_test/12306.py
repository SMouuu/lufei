import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


opt=Options()
opt.add_argument("--disable-blink-features=AutomationControlled")
web=Chrome(options=opt)
web.get("https://kyfw.12306.cn/otn/resources/login.html")
web.implicitly_wait(10)
web.find_element(By.XPATH,"//*[@id='toolbar_Div']/div[2]/div[2]/ul/li[1]/a").click()
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys("123")
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys("1234567")

#点击登录
web.find_element(By.XPATH,'//*[@id="J-login"]').click()
time.sleep(1)
btn=web.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,xoffset=300,yoffset=0).perform()