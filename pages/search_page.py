
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

# 继承父类BasePage
class BaiduPage(BasePage):

    @property
    def search_input(self):
        return self.driver.find_element(By.ID, 'chat-textarea')

    @property
    def search_button(self):
        return self.driver.find_element(By.ID,'chat-submit-button')

    @property
    def change_button(self):
        return self.driver.find_element(By.CLASS_NAME,'c-icon.refresh-icon')

    @property
    def change10thtitle(self):
        return self.driver.find_element(By.CLASS_NAME,'title-content-index.c-index-single.c-index-single-hot10')

    @property
    def news_button(self):
        return self.driver.find_element(By.CLASS_NAME,'mnav.c-font-normal.c-color-t')

    @property
    def knowmore_button(self):
        # return self.driver.find_element(By.XPATH,"//*[@title = '点击一下，了解更多']")
        # return self.driver.find_element(By.ID,'s_lg_img_new')
        # return self.driver.find_element(By.NAME, 'mp')
        return self.driver.find_element(By.ID,'lg')

    @property
    def news_button(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT,'新闻')


# 另一个页面也需要用到父类-BasePage
class MailPage(BasePage):

    def account_page(self):
        pass



