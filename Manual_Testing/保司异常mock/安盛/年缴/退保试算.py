# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Mock_SurrenderTrial:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "mock_host")

    def Mock_SurrenderTrial(self):
        url = "/hlcpTest/webservice/as/mock/Surrender_Trial/year"
        request_url = self.host + url
        body = {}
        return SendMethod.Post_DataJson(url=request_url, json=body)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Mock_SurrenderTrial().Mock_SurrenderTrial()
    print(f'[{CO.Execution_Time()}]\n{Res}')
