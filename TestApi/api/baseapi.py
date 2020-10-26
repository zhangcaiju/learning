from jsonpath import jsonpath
import requests


class BaseApi:
    def send_requests(self, req:dict):  # :dict为req的注解，无实际意义
        """
        对requests进行二次封装
        """
        # req = {
        #     "method": "get",
        #     "url": "xxx",
        #     "params": {},
        #     "json": {}
        # }
        # 等同于requests.request(method=get, url="xxxxx", params={}, json={})
        # **req 为字典解包
        return requests.request(**req)

    def base_jsonpath(self, obj, json_expr):
        return jsonpath(obj, json_expr)