from TestPO.pages.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        # 初始化企业微信主页面
        self.main = MainPage()

    def test_add_member(self):
        # 1.从首页跳转到添加成员页面   2.添加成员
        namelist = self.main.go_to_add_member().add_member('肯德超', '222', '12333344556').save_member().get_member_list()
        assert "肯德超" in namelist

    def test_add_member_failed(self):
        namelist = self.main.go_to_add_member().add_member('孙德超', '222', '12433344556').cancle_member().get_member_list()
        assert "孙德超" not in namelist

    def test_contact_member(self):
        # 1.从首页跳转到通讯录页面   2.从通讯录跳转到添加成员页面   3.添加成员
        namelist = self.main.go_to_contact_page().go_to_add_member().add_member('肯德超1', '2222', '12337344556').save_member().get_member_list()
        assert '肯德超1' in namelist

    def teardown(self):
        self.main.driver.quit()