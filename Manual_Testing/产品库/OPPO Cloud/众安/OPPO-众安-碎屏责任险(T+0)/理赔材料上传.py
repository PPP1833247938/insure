# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Material_upload:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Material_upload(self):
        url = "/issuingmc/channelapi/claim/machine/file/upload"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "PI07306240424948884531",  # 保单号
                "MaterialName": "维修前照片.jpg",  # 材料名，示例：xxx.png
                "MaterialType": "2",  # 材料类型：1 - 证件照 2、维修前照片 3、维修后照片
                "MaterialFileType": "FILE_URL",  # 材料文件类型：FILE_URL - 文件地址、BASE64 - base64数据流
                "Data": "https://picnew13.photophoto.cn/20190527/ziranfengjingtupiansucaibizhishanshuifengjing-33283943_1.jpg"
                # 数据
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0043",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Material_upload().Material_upload()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
