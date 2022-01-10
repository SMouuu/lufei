# BOSS直聘
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import json
import requests




def base64_api(img, uname="q6035945", pwd="q6035945", typeid=27) :
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]



web = Chrome()
web.get("https://login.zhipin.com/?ka=header-login")
web.implicitly_wait(10)
web.find_element(
    By.XPATH, '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/form/div[3]/span[2]/input').send_keys("")
web.find_element(
    By.XPATH, '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/form/div[4]/span/input').send_keys("")
web.find_element(By.XPATH, '//*[@id="pwdVerrifyCode"]/div').click()
# 获取到验证码
verify_div = web.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/div')
verify_div.screenshot("tu.png")
tu = verify_div.screenshot_as_base64
print(tu)
verify_code=base64_api(tu)
print(type(verify_code))
for p in verify_code.split("|"):
    x=int(p.split(",")[0])
    y=int(p.split(",")[1])
    ActionChains(web).move_to_element_with_offset(verify_div,xoffset=x,yoffset=y).click().perform()
web.close()
