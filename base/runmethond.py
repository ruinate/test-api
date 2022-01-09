import json
import requests

requests.packages.urllib3.disable_warnings()


class RunMethod:

    def post_main(self, url, data, header=None):

        res = None
        if header != None:

            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def put_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.put(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.put(url=url, data=data, verify=False)
        return res.json()

    def delete_main(self,url, header=None):
        res = None
        if header != None:
            res = requests.delete(url=url, headers=header)
        else:
            res = requests.delete(url=url)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        elif method == 'Put':
            res = self.put_main(url, data, header)

        elif method == 'Delete':

            res = self.delete_main(url, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    data = {
        'cart': '11'
    }
    run = RunMethod()
    run_test = run.run_main("Post", url=url, data=data)
    print(run_test)
