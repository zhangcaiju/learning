from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            if self._base_url != "":
                self.driver.get(self._base_url)
            self.driver.implicitly_wait(10)
        else:
            # : WebDriver注解，无实际意义
            self.driver: WebDriver = driver_base

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def wait_for_clickable(self, element):
        # 显示等待元素可被点击，适用于元素不可被点击的报错
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
