# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")


class Callback:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "callback_host")

    def Callback(self):
        url = "/issuingmc/channelopenapi/zan/20210707/policyNotice"
        request_url = self.host + url
        body = (
            "0aMckP7WBgJXrEul7285gDewOe9b/2rr3fTlHE5tJaaVRELAOOfSSBGcPnaJqlANoGhca8u3UsSNCUfUo3N/K+fdB2iW2Qj7+sbei+u3i1"
            "PH+ImZezkOJgoFpBp09VRnrlkRtJz4NMLvm6K0ZQIVfJ2eEAERl19HexiaiGWDmh94jHl4vzBE9+I7SG/Tf0a7A67vnIWg9d8hLGFe8a03"
            "LmZ0iuMpWTp6/QevA5JX+AfoiqTjnUNQVoh15ED53hiw")
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.Post_DataJson(url=request_url, json=body)


"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
