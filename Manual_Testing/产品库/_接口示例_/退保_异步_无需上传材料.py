# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Synchronous_surrender:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Synchronous_surrender(self):
        url = "/issuingmc/channelapi/policy/cancelConfirm"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "H231121004148080112535",  # 保单号
                "CancelDate": CO.Time(),  # 退保申请时间
                "RefundPremium": "0.00",  # 退保金额（不一定等于实际退费金额）
                "Currency": "CNY",  # 币种
                "Type": "NORMAL",  # 退保类型： 正常退保 - NORMAL ，协商退保 - NEGOTIATE
                "ReasonRemark": "测试单,退保",  # 退保原因
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0027",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Synchronous_surrender().Synchronous_surrender()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
