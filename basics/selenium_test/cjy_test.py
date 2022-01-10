from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client 
import time
#超级鹰干超级鹰


web=Chrome()
web.get('http://www.chaojiying.com/user/login/')
#破解验证码
png=web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('18614075987', 'q6035945', '927541')
result = chaojiying.PostPic(png, 1902)
print(result)
v_code=result['pic_str']

web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("18614075987")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("q6035945")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(v_code)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
time.sleep(5)

