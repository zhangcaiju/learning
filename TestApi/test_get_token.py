import requests


class TestGetToken:
    def test_get_token(self):
        '''
        获取access_token GET
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "ww4bb20009b7935eeb",
            "corpsecret": "GlaFuT0CKO5WU4ujQ_eSvvvKVRGBSBAyhyHHCEup8Sk"
        }
        r = requests.get(url=url, params=params)
        print(r.json())
