import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_baidu_ui.pages.search_page import BaiduPage


def test_switchto_hotsearch(driver):
    '''百度热搜'''
    url = 'https://www.baidu.com/'  
    page = BaiduPage(driver)

    page.open(url)

    list_windows = driver.current_window_handle
    print(driver.title)
    driver.implicitly_wait(2)

    page.knowmore_button.click()

    allhandles = driver.window_handles
    for handle in allhandles:
        if handle != list_windows:
            driver.switch_to.window(handle)
            print(driver.title)
            assert '百度热搜' in driver.title
            driver.close()

    driver.switch_to.window(list_windows)
    driver.switch_to.default_content()
    time.sleep(2)

def test_switchto_commonapplication(driver):
    '''新闻链接'''
    url = 'https://www.baidu.com/'
    page = BaiduPage(driver)

    page.open(url)

    list_windows = driver.current_window_handle
    print(driver.title)
    driver.implicitly_wait(2)

    page.news_button.click()

    allhandles = driver.window_handles
    for handle in allhandles:
        if handle != list_windows:
            driver.switch_to.window(handle)
            print(driver.title)
            assert '百度新闻' in driver.title
            driver.close()

    driver.switch_to.window(list_windows)
    driver.switch_to.default_content()

if __name__ == '__main__':
    current = time.strftime("%Y%m%d_%H%M%S_",time.localtime(time.time()))

    html_report = './test_report/' + current + 'report.html'
    pytest.main(["-q","--html",html_report])
