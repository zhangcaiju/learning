from selenium.webdriver.common.by import By
from TestPO.pages.base_page import BasePage
from TestPO.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    # _开头，是为了参数的私有化，让其他调用方.的时候看不到
    _username = (By.ID, 'username')
    _memberAdd_acctid = (By.ID, 'memberAdd_acctid')
    _memberAdd_phone = (By.ID, 'memberAdd_phone')
    _cancle = (By.CSS_SELECTOR, "[node-type='cancel']")

    def add_member(self, name, acctid, phone):
        # *self._username 解元组操作
        self.find(*self._username).send_keys(name)
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(phone)
        # return self 是为了实现返回当前页面时，依然可以实现链式调用
        # 相当于 别人调用时：add_member().save_member() 就等同于 self.save_member()
        return self

    def save_member(self):
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self.driver)

    def cancle_member(self):
        self.find(By.CSS_SELECTOR, '.js_btn_cancel').click()
        self.wait_for_clickable(self._cancle)
        self.find(*self._cancle).click()
        return ContactPage(self.driver)

    def save_and_add(self):
        self.find(By.XPATH, '//*[@id="js_contacts300"]/div/div[2]/div/div[4]/div/form/div[1]/a[1]').click()
