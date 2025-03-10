# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")
"""太平碎屏险理赔,先申请再上传材料"""


class Claim_application:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def Claim_application(self):
        url = "/issuingmc/channelapi/claim/machine/report"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyNo": "EP202403640000023971",  # 保单号
                "ReportOrderNo": CO.RandomStr().create(),  # 报案订单号 (接口幂等字段)
                "ReporterName": "彦祖",  # 报案人姓名
                "ReporterPhone": "13410506136",  # 报案人联系电话
                "ReportDate": "20240425000000",  # 报案时间
                "ReportProvinceName": "广东省",  # 报案地 - 省
                "ReportCityName": "深圳市",  # 报案地 - 市
                "ReportAreaName": "南山区",  # 报案地 - 区
                "ReportAddrDetail": "梦海大道",  # 报案地 - 具体地址，比如门店地址等
                "ReportSource": "1",  # 报案来源渠道：1 - OPPO
                "ReportRepairCharge": "2000.00",  # 报案维修费用
                "ReportServiceCharge": "0.00",  # 报案服务费
                "DamageDate": "20240425000000",  # 出险时间
                "DamageDetail": "测试单,反正就是坏了!",  # 出险详细经历（包括故障原因）
                # "MaterialList": ["O8575020403979272203","O8575020403979272204"],  # 理赔材料Id列表 [“543534534”,”4324234234”]
                "RepairCompleteDate": "20240428000000",  # 维修完成时间
                "Reserve1": "CN097013"  # 保留字段1（网点编码）
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0044",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Claim_application().Claim_application()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
