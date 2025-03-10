# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Policy_printing:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Policy_printing(self):
        url = "/issuingmc/channelapi/policy/print"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "H231226004398300146393",  # 保单号
                "CertificateType": "100"  # 保单打印类型100-主保单,200-其它
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0012",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Policy_printing().Policy_printing()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
