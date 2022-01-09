from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    web = Chrome()
    url = "http://www.lagou.com"
    web.get(url)
    print(web.title)
    x_btn = web.find_element_by_xpath('//*[@id="cboxClose"]')
    x_btn.click()
    time.sleep(1)
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
        break