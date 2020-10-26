from TestApi.api.baseapi import BaseApi


class GetToken(BaseApi):
    def get_token(self, corpcecret):
        corpid = "ww4bb20009b7935eeb"
        corpsecret = "GlaFuT0CKO5WU4ujQ_eSvvvKVRGBSBAyhyHHCEup8Sk"
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        }
        r = self.send_requests(req)
        self.token = r.json()["access_token"]
        return self.token
