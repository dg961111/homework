import requests


class BaseApi:
    HOST = "https://qyapi.weixin.qq.com"
    CORP_ID = "ww85665d92492dddf7"
    CORP_SECRET = "9jXU8E-NRTXc7dUa5X77PFuSdnRFcd2Bp31hlo9AHYA"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        path = "/cgi-bin/gettoken"
        data = {
            "corpid": self.CORP_ID,
            "corpsecret": self.CORP_SECRET
        }
        re = requests.post(self.HOST + path, json=data)
        token = re.json().get("access_token")
        return token

    def http_post(self, path, **kwargs):
        return requests.post(self.HOST + path, **kwargs)

    def http_get(self, path, **kwargs):
        return requests.get(self.HOST + path, **kwargs)
