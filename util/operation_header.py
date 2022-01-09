import json
from util.operation_json import OperationJson
from base.runmethond import RunMethod
import requests


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_token(self):
        '''
        获取登录返回的token
        '''

        # print(json.loads(s.text)["token"])
        if self.response in ['err']:
            pass
        else:
            token = {"data": {"Authorization": 'Bearer  '+self.response['data']['jwt_token']}}
            return token

    def get_response_zd(self):
        '''
        获取登录返回的返回字段
        '''

        # print(json.loads(s.text)["token"])

        zd = {"data": {"expires_in": self.response["expires_in"]}}
        return zd

    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())


if __name__ == '__main__':
    url = "http://www.em.liufei.love/api/user/login/"

    data = {
        "username": "fzf123",
        "password": ""
    }
    run_method = RunMethod()
    # res = json.dumps(requests.post(url, data).json())
    res = run_method.run_main('Post', url, data)
    print(res)
    op = OperationHeader(res)
    op.write_token()
