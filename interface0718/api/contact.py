from typing import List
from interface0718.api.base_api import BaseApi


class ContactApi(BaseApi):

    def add(self, userid, name, department: List[int], **kwargs):
        path = f"/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "access_token": self.token,
            **kwargs
        }
        re = self.http_post(path, json=data)
        return re

    def update(self, userid, **kwargs):
        path = f"/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": userid,
            **kwargs
        }
        re = self.http_post(path, json=data)
        return re

    def delete(self, userid):
        path = "/cgi-bin/user/delete"
        data = {
            "userid": userid,
            "access_token": self.token
        }
        re = self.http_get(path, params=data)
        return re

    def get(self, userid):
        path = "/cgi-bin/user/get"
        data = {
            "userid": userid,
            "access_token": self.token
        }
        re = self.http_get(path, params=data)
        return re

    # def get_all_member(self):
    #     pass
