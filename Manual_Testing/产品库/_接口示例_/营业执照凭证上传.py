# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class License_upload:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def License_upload(self):
        url = "/issuingmc/channelapi/license/file/upload"
        request_url = self.host + url
        body = {
            "Data": {
                "AgencyPolicyRef": "3U9TTfLYG6FbfUgm",  # 对应大订单号
                "ApplyPolicyRef": "ET202300000009133815",  # 对应大投保单号
                "File":
                    {
                        "FileName": "营业执照.jpg",  # 带后缀名称的文件名
                        "FileType": "FILE_URL",  # 文件类型，FILE_URL 文件url；BASE64，base64编码格式
                        "Data": "https://waizi.org.cn/uploadfile/201402/22/220466577.jpg"  # 文件地址
                    }
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0051",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = License_upload().License_upload()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
