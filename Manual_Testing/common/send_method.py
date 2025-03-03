# -*- coding: utf-8 -*-
import requests, json
from Manual_Testing.common.encryption_decryption import AesDensity
from Manual_Testing.common.communal import JsonFormatting
from Manual_Testing.common.operation_config import Config
from Manual_Testing.Environment import Environment

config = Config("config.ini")


class PrePose:
    """初始化环境请求头信息含aes秘钥"""

    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")


class SendMethod:
    @staticmethod
    def get(url, params=None, headers=None):
        try:
            response = requests.get(url=url, params=params, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_data(url, data=None, headers=None):
        try:
            response = requests.post(url=url, data=data, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_datax(url, data=None, headers=None):
        try:
            response = requests.post(url=url, data=data, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.text
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_json(url, json=None, headers=None):
        try:
            response = requests.post(url=url, json=json, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.json()
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def post_jsonx(url, json=None, headers=None):
        try:
            response = requests.post(url=url, json=json, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            result["ResponseBody"] = response.text
            return JsonFormatting(result)
        except:
            result = None
            return result

    @staticmethod
    def PostData_aes(key, url, data=None, headers=None):
        try:
            aes = AesDensity(key)
            Data = aes.encrypt(json.dumps(data, ensure_ascii=False))
            response = requests.post(url=url, data=Data, headers=headers)
            result = {}
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int((response.elapsed.microseconds) / 1000)
            if response.status_code == 200:
                result["ResponseBody"] = json.loads(aes.decrypt(response.text))
                return JsonFormatting(result)
            else:
                try:
                    result["ResponseBody"] = json.loads(response.text)
                    return JsonFormatting(result)
                except:
                    result["ResponseBody"] = response.text
                    return JsonFormatting(result)
        except:
            result = None
            return result


if __name__ == '__main__':
    """
    """
