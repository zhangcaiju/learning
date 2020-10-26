from TestPO.pages.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        department_list = self.main.go_to_contact_page().add_department("11").save_department().get_department_list()
        assert "11" in department_list

    def teardown(self):
        self.main.driver.quit()
