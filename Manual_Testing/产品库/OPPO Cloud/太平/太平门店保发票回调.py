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
        url = "/issuingmc/channelopenapi/tp/store/invoice/callback"
        request_url = self.host + url
        body = f"""<?xml version="1.0" encoding="UTF-8"?>
                    <document>
                        <request>
                            <head>
                                <productCode>0201797</productCode>
                                <businessType>invoice</businessType>
                                <transTime>{CO.Execution_Time()}</transTime>
                                <agencyCode>BBK</agencyCode>
                                <orderNo>O162220240512163325972</orderNo>
                            </head>
                            <body>
                                <policyno>EP202403202635000123</policyno>
                                <invoiceurl>http://dzdz.cbit.com.cn/#/S?d=950497fb585dbb3d</invoiceurl>
                            </body>
                        </request>
                    </document>
               """
        print(f'[{CO.Execution_Time()}]-Request:\n{body}')
        return SendMethod.post_datax(url=request_url, data=body)


"""修改需要回调policyno保单号即可;仅电子发票需要回调"""
"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
