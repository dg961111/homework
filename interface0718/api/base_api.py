import requests


class BaseApi:

    def __init__(self):
        self.host = "https://qyapi.weixin.qq.com"
        self.corp_id = "ww85665d92492dddf7"
        self.secret_key = "9jXU8E-NRTXc7dUa5X77PFuSdnRFcd2Bp31hlo9AHYA"
        self.token = self.get_token()

    def get_token(self):
        path = "/cgi-bin/gettoken"
        data = {
            "corpid": self.corp_id,
            "corpsecret": self.secret_key
        }
        re = requests.post(self.host + path, json=data)
        token = re.json().get("access_token")
        return token

