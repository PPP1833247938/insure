# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Surrender_trial:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Surrender_trial(self):
        url = "/issuingmc/channelapi/policy/premiumCalculation"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "PI07306230824779982661",  # 保单号
                "CancelDate": CO.Time(),  # 退保申请日期
                "CancelFlag": "0"  # 退保说明(0-主动，1-被动)
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0016",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Surrender_trial().Surrender_trial()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
