from selenium.webdriver.common.by import By
from TestPO.pages.add_member_page import AddMemberPage
from TestPO.pages.base_page import BasePage
from TestPO.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    _add_member = (By.CSS_SELECTOR, '.index_service_cnt_item_title')
    _menu_contact = (By.ID, 'menu_contacts')

    def go_to_contact_page(self):
        self.find(*self._menu_contact).click()
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.find(*self._add_member).click()
        # 第二次初始化，子类AddMemberPage初始化
        return AddMemberPage(self.driver)
