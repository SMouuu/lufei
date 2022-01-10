from selenium.webdriver import Chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#配置无头信息
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    web = Chrome()
    url = "http://www.lagou.com"
    web.get(url)
    print(web.title)
    x_btn = web.find_element_by_xpath('//*[@id="cboxClose"]')
    x_btn.click()
    time.sleep(1)
    # web.implicitly_wait(10)
    
    #selenium执行js
    web.execute_script(
        '''
            var a=document.getElementsByClassName("un-login-banner")[0];
            a.parentNode.removeChild(a);
        '''
    )
    web.find_element_by_xpath(
        '//*[@id="search_input"]').send_keys("python", Keys.ENTER)
    time.sleep(2)
    div_list=web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
    for i in div_list:
        h=i.find_element_by_xpath('./div[1]/div[1]/div[1]/a')
        h.click()
        web.switch_to.window(web.window_handles[-1])
        job_tetail=web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div')
        print(job_tetail.text)
        web.close()
        web.switch_to.window(web.window_handles[0])
    web.quit()#关闭浏览器


# 下拉列表处理

#配置无头骑士
# opt=Options()
# opt.add_argument("--headless")
# opt.add_argument("--disable=gpu")
# web = Chrome(options=opt)
# sel = web.find_element(By.XPATH, '')
# sel_new = Select(sel)
# print(len(sel_new.options))  # 所有选项
# for i in range(len(sel_new.options)):
#     sel_new.select_by_index(i)
# # sel_new.select_by_value()
# # sel_new.select_by_visible_text()
# 927541