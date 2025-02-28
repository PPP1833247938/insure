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
        url = "/issuingmc/channelopenapi/directPay/contract/callback"
        request_url = self.host + url
        body = (
            "cvME+R5gA1eZHnjJMNCX0rhrIy4fhYt5srGtZrY5pfJU8c420P+FOktrf62QENUKJntzLwfYA1suGizc1QwEcu2NA/"
            "uDSfHO0TtPikaHFapZle+v4hb5mvoUz6hMqimMUJSn5uBPGgX5nyoxM/IEhmnVhJNjTVL11muuUj+1TH0Y68yXvTYqql"
            "bL0U9RzLP2MK9iNRIqMEQ1/hwWhjpiNHuOYXHB5tX8q/rzOQzft1GyEPt50ratoRWIOJBe6syVLtWmutRogGgwA77SAg"
            "NXXqCXoGTQup/tbetbtxMv/yPj7P84gexZfXFrscumVaA3ZLftmS6MV6SfQJkg+j4fOGaTzjeFsI1hCkj+xykFsY9I9cY"
            "gBw0IpURmGfAaGkjI8zPRlE1DrkRXSkoW0RtEPQ==")
        print(f'[{CO.Execution_Time()}]-Request:\n{body}')
        return SendMethod.post_data(url=request_url, data=body)


"""请求成功后,查看日志是否有回调推送给OPPO"""
if __name__ == "__main__":
    Res = Callback().Callback()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
