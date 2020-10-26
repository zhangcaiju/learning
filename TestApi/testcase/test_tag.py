import yaml

from TestApi.api.tag import Tag


class TestTag():
    def setup_class(self):
        self.tag = Tag()
        config_info = yaml.safe_load(open("config.yaml"))
        self.tag.get_token(config_info["token"]["department_secret"])

    def test_creat_tag(self):
        self.tag.creat_tag(1)
        list = self.tag.get_tag_list()
        print(list)
        assert  "法师" in self.tag.base_jsonpath(list, "$..tagname")

    def test_update_tag_name(self):
        self.tag.update_tag_name(1)
        list = self.tag.get_tag_list()
        assert "辅助" in self.tag.base_jsonpath(list, "$..tagname")

    def test_delete_tag(self):
        self.tag.delete_tag(1)
        list = self.tag.get_tag_list()
        print(list)
        assert 1 not in self.tag.base_jsonpath(list, "$..tagid")

    def test_get_tag_member(self):
        print(self.tag.get_tag_member(2))

    def test_add_tag_member(self):
        # 此处2指的是tagid，添加的部门id在tag.py
        self.tag.add_tag_member(2)

    def test_delete_tag_member(self):
        self.tag.delete_tag_member(2)

    def test_get_tag_list(self):
        print(self.tag.get_tag_list())