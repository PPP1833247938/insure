# -*- coding: utf-8 -*-
from Manual_Testing.common.operation_config import Config
import json, sys
from Manual_Testing.common.send_method import SendMethod
from Manual_Testing.Environment import Environment
from Manual_Testing.common import communal as CO

config = Config("config.ini")
"""
百万魔方升降级产,产品码:TK20220623
钩子版,年缴计划码:TK202206230101
钩子版,月缴计划码:TK202206230102
基础版,年缴计划码:TK202206230201
基础版,月缴计划码:TK202206230202
降级版,年缴计划码:TK202206230301
降级版,月缴计划码:TK202206230302
"""


class JKX_underwriting:
    def __init__(self):
        self.environment = Environment
        self.host = config.get_value(self.environment, "host")
        self.headers = json.loads(config.get_value(self.environment, "headers"))
        self.ChannelCode = config.get_value(self.environment, "ChannelCode")
        self.key = config.get_value(self.environment, "key")

    def JKX_underwriting(self):
        url = "/issuingmc/channelapi/insure/check"
        request_url = self.host + url
        body = {
            "Data": {
                "Policy": {  # 保单信息
                    "AgencyPolicyRef": CO.RandomStr().create(),  # 第三方订单号
                    "PlanCode": "TK202206230102",  # 计划代码;
                    "IssueDate": CO.Time(),  # 出单时间
                    "EffectiveDate": CO.Tomorrow(),  # 生效时间               注:本产品支持次日零时生效或T+30生效
                    "ExpireDate": CO.SeveralYears(),  # 失效时间# 注(保单未失效,续保前需要现在数据库修改有效期后再续保)
                    "GroupSize": "1",  # 被保人个数
                    "Currency": "CNY",  # 币别类型
                    "PaymentType": "2",  # 缴费方式：1-年缴2-月缴3-趸缴4-免缴
                    "TotalPremium": "482.40",  # 总保费
                    "FaceAmount": "300000.00",  # 保额注：1、保额可批增为初始保额2、医疗险多种条款为保额之和
                    "InstallmentNumber": "12",  # 分期期数 (分期产品必传)
                    "ResponsibilityList": None,  # 组合责任列表(部分产品必传) 示例： [“010231”,”010232”]
                    "InstallmentNo": None  # 期数，分期趸交产品必传
                },
                "PolicyHolder": {  # 投保人信息
                    "PolicyHolderType": "1",  # 投保人类型1-个人2-企业或者机构
                    "PolicyHolderName": "刘洋",  # 用户姓名/企业名
                    "PolicyHolderSex": None,  # 性别（0女，1男，2其它）
                    "PHIdType": "01",
                    # 证件类型01身份证,02户口簿,03护照,04军官证,05驾驶执照,06港澳返乡证,07台胞证,08出生证,09统一社会信用代码,10纳税人识别号,11其他)
                    "PHIdNumber": "54212919980107164X",  # 证件号/企业编号
                    "PHBirthDate": "19980107000000",  # 出生日期 投保类型为2不传
                    "PHTelephone": "13777775688",  # 手机号 投保类型为2非必传
                    "PHEmail": None,  # 邮箱
                    "PHAddress": None  # 详细地址
                },
                "InsuredList": [  # 被保人信息列表
                    {
                        "InsuredId": "7",  # 被保险人唯一Id，用来确认该保单下被保险人的唯一性
                        "InsuredName": "刘洋",  # 用户姓名/企业名
                        "Gender": None,  # 性别（0女，1男，2其它）
                        "InsuredType": "D1",  # 被保险人类型(参考附录 证件类型（个人）) 特殊说明下必传
                        "Type": "1",  # 被保人类型1-个人2-企业或者机构（默认个人）
                        "IdType": "01",  # 证件类型(参考附录 证件类型（个人）)投保类型为2不传
                        "IdNumber": "54212919980107164X",  # 证件号/企业编号
                        "BirthDate": "19980107000000",  # 出生日期 投保类型为2非必传
                        "Mobile": None,  # 手机号投保类型为2非必传
                        "Email": None,  # 邮箱
                        "ResideAddress": None,  # 详细地址
                        "PolicyholderInsuredRelation": "01",  # 被保人与投保人关系(01本人,02配偶,07儿女,08父母,22其他) 投保类型为2时不传
                        "SocialSecurityFlag": "0",  # 有无社保0无1有 健康险必传，意外险非必传 投保类型为2时不传
                        "UnderwritingType": "0",  # 智能核保问卷告知 支持智能核保产品必传0-全无 1-部分是 投保类型为2时不传
                        "UnderwritingQuestionList": None,  # 智能核保问卷(智能核保问卷部分是时必填 ) 投保类型为2时不传
                        "OccupationCode": None  # 职业编码，部分产品必传，每个产品职业编码列表独立
                    }
                ],
                "AutoRenewalFlag": "1",
                "InstallmentList": [  # 分期信息列表，缴费方式为月缴PaymentType=2时必填
                    {
                        "InstallmentNum": "12",  # 分期数，如月缴12期
                        "InstallmentNo": "1",  # 分期号，按照约定传值；只有首期保费核保的产品，分期号固定值为1
                        "InstallmentPremium": "2.30",  # 对应分期号的保费，当前产品固定为首期保费
                        "EachPremium": "2.30"  # 分期保费
                    }
                ]
            },
            "ChannelCode": self.ChannelCode,
            "RequestID": CO.RandomStr().create(),
            "RequestType": "0006",
            "Version": "1.0.0"
        }
        print(f'[{CO.Execution_Time()}]-Request:\n{CO.JsonFormatting(body)}')
        return SendMethod.PostData_aes(key=self.key, url=request_url, data=body, headers=self.headers)


if __name__ == "__main__":
    sys.stdout = CO.Logger()
    Res = JKX_underwriting().JKX_underwriting()
    print(f'[{CO.Execution_Time()}]-Response:\n{Res}')
