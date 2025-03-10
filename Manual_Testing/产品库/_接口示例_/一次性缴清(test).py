# -*- coding: utf-8 -*-
import json, sys
from Manual_Testing.common.send_method import PrePose, SendMethod
from Manual_Testing.common import communal as CO


class Paid_up(PrePose):
    def Paid_up(self):
        url = "/issuingmc/channelapi/insure/renewalAll"
        request_url = self.host + url
        body = {
            "Data": {
                "PolicyRef": "PI07306230824779981301",  # 需要缴费的保单号码
                "Type": "0",  # 0-月缴一次性缴清，仍是月缴保单；1- 月缴缴清转年缴
                "PaymentDate": "20230221000000",  # 支付完成时间
                "Currency": "CNY",  # 币别
                "PaymentMethod": "2",  # 支付方式：1-支付宝；2-微信支付；3-通联支付；4-快钱支付
                "PaymentFlowNum": CO.RandomStr().create(),  # 支付流水号/商户订单号（第三方支付流水号）
                "StartInstallmentNo": "4",  # 开始缴费分期号
                "PaymentPremium": "54.90",  # 实际支付总保费
                "DiscountPremium": "0",  # 优惠总金额(无优惠为0)
                "MerchantOrderNum": None  # 备注无
            },
            "RequestID": CO.RandomStr().create(),
            "Version": "1.0.0",
            "ChannelCode": self.ChannelCode,
            "RequestType": "0035"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = Paid_up().Paid_up()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
