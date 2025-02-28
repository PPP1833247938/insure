# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class IMEI_correction:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def IMEI_correction(self):
        url = "/issuingmc/channelapi/modify/machine/imei"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "PI07306240361908133406",  # 保单号
                "ModifyNo": CO.RandomStr().create(),  # 批改单号 (接口幂等字段)
                "OldProductSerialNo": "TenSergBYCcTxamX",  # 原序列号
                "NewProductSerialNo": "TenSergBYCcTxamX1"  # 新序列号
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0045",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = IMEI_correction().IMEI_correction()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
