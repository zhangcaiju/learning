from selenium.webdriver.common.by import By
from TestPO.pages.base_page import BasePage


class ContactPage(BasePage):
    _add_member = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    _cancle = (By.CSS_SELECTOR, ".js_btn_cancel")
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _click_add = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    _department = (By.CSS_SELECTOR, '.js_create_party')
    _department_name = (By.CSS_SELECTOR, 'input[name="name"]')
    _select_department = (By.CSS_SELECTOR, '.js_parent_party_name')
    _save_department = (By.CSS_SELECTOR, '[d_ck="submit"]')
    _cancle_department = (By.CSS_SELECTOR, '[d_ck="cancle"]')
    _departmentliebiao = (By.CSS_SELECTOR, '.jstree-anchor')

    def go_to_add_member(self):
        # 解决循环导入问题
        from TestPO.pages.add_member_page import AddMemberPage
        self.wait_for_clickable(self._add_member)
        # 进入死循环
        while True:
            self.find(*self._add_member).click()
            # 报错捕获，执行except循环点击找元素操作，直到找到为止
            try:
                # 找到添加成员页面的某个元素（取消按钮）
                res = self.find(*self._cancle)
                if res is not None:
                    break
            except:
                print("暂时没找到")
        return AddMemberPage(self.driver)

    def get_member_list(self):
        ele = self.finds(*self._member_list)
        return [name.text for name in ele]

    def add_department(self, name):
        self.find(*self._click_add).click()
        self.find(*self._department).click()
        self.find(*self._department_name).send_keys(name)
        self.find(*self._select_department).click()
        dep = self.find(By.CSS_SELECTOR, '[class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]').click()
        # if dep is not None:
        #     dep[0].click()
        #     print(dep[0].text)
        # departmentlist = self.finds(By.CSS_SELECTOR,
        #                            '[class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]')
        # print(departmentlist)
        return self

    def get_department_list(self):
        departmentlist = self.finds(*self._departmentliebiao)
        return [departmentname.text for departmentname in departmentlist]

    def save_department(self):
        self.find(*self._save_department).click()
        return ContactPage(self.driver)

    def cancle_department(self):
        self.find(*self._cancle_department).click()
        return ContactPage(self.driver)
