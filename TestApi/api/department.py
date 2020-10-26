from TestApi.api.wework import GetToken


class Department(GetToken):
    def creat_department(self, department_id):
        data = {
            "name": "德玛西亚",
            "parentid": "1",
            "id": department_id
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
            "json": data
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = self.send_requests(req)
        return r.json()

    def update_department(self, department_id):
        data = {
            "name": "艾欧尼亚",
            "parentid": "1",
            "id": department_id
        }
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}&id={department_id}",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def delete_department(self, department_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        }
        r = self.send_requests(req)
        return r.json()

    def get_department_list(self):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        }
        r = self.send_requests(req)
        return r.json()
