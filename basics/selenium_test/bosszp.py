#BOSS直聘
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

web=Chrome()
web.get("https://login.zhipin.com/?ka=header-login")
web.implicitly_wait(10)
web.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/form/div[3]/span[2]/input').send_keys("")
web.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/form/div[4]/span/input').send_keys("")
web.find_element(By.XPATH,'//*[@id="pwdVerrifyCode"]/div').click()
#获取到验证码
verify_div=web.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div/div')
verify_div.screenshot("tu.png")
tu=verify_div.screenshot_as_base64
print(tu)
web.close()