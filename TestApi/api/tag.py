from TestApi.api.wework import GetToken


class Tag(GetToken):
    def creat_tag(self, tag_id):
        data = {
            "tagname": "法师",
            "tagid": tag_id
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def update_tag_name(self, tag_id):
        data = {
            "tagid": tag_id,
            "tagname": "辅助"
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def delete_tag(self, tag_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        }
        r = self.send_requests(req)
        return r.json()

    def get_tag_member(self, tag_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}"
        }
        r = self.send_requests(req)
        return r.json()

    def add_tag_member(self, tag_id):
        data = {
            "tagid": tag_id,
            "partylist": [1]
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def delete_tag_member(self, tag_id):
        data = {
            "tagid": tag_id,
            "partylist": [1]
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def get_tag_list(self):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        }
        r = self.send_requests(req)
        return r.json()
