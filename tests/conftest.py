#!/usr/bin/env python
# -*- coding:utf-8-*-
"""
=================================
created on June 27th,2025
实现百度网站的Web UI自动化测试
=================================
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def driver():
    url = 'https://www.baidu.com'

    global driver
    # driver = webdriver.Edge(executable_path='D:\\zheng\\driver\\msedgedriver.exe')
    driver = webdriver.Chrome(executable_path='D:\zheng\driver\chromedriver.exe')
    driver.maximize_window()
    driver.get(url)

    return driver


@pytest.fixture(scope="function")
def login(driver):
    pass


@pytest.fixture(scope="function")
def logout(driver):
    pass


@pytest.fixture(scope="session", autouse=True)
def driver_close():
    yield driver
    driver.close()
    driver.quit()

