import yaml

from TestApi.api.department import Department


class TestAddDepartment:
    def setup_class(self):
        self.department = Department()
        config_info = yaml.safe_load(open("config.yaml"))
        # 通过传入不同的secret获取不同的token权限，给不同的业务测试用例使用。
        # 当secret 和业务紧密相关， 应该抽离出来维护
        self.department.get_token(config_info["token"]["department_secret"])
        # self.department.get_token()

    def test_add_department(self):
        '''
        创建部门 POST
        '''
        self.department.creat_department(3)
        list = self.department.get_department_list()
        print(list)
        assert "德玛西亚" in self.department.base_jsonpath(list, "$..name")

    def test_update_department(self):
        """
        更新部门 POST
        """
        self.department.update_department(3)
        list = self.department.get_department_list()
        assert "艾欧尼亚" in self.department.base_jsonpath(list, "$..name")

    def test_delete_department(self):
        """
        删除部门 GET
        """
        self.department.delete_department(3)
        list = self.department.get_department_list()
        assert 3 not in self.department.base_jsonpath(list, "$..id")
