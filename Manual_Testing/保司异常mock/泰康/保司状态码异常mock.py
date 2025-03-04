# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Abnormal:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "mock_host")

    def Abnormal(self):
        url = "/hlcpTest/tk/mock/abnormal2"
        request_url = self.host + url
        body = {}
        return SendMethod.Post_DataJson(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Abnormal().Abnormal()
    print(f'[{CO.Execution_Time()}]\n{Res}')
