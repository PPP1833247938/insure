[2025-02-12 14:52:13]-Request:
{
    "Data": {
        "PolicyRef": "PI07306250225263683839",
        "CancelDate": "20250212145213",
        "CancelPremium": null,
        "Currency": null,
        "Type": null,
        "ReasonRemark": null
    },
    "ChannelCode": "O00001",
    "RequestID": "ZIDING6EGWJ5NZZJGRL6WZSH8ATX7UCB",
    "RequestType": "0017",
    "Version": "1.0.0"
}
[2025-02-12 14:52:13]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 150,
    "ResponseBody": {
        "RequestID": "ZIDING6EGWJ5NZZJGRL6WZSH8ATX7UCB",
        "RequestType": "0017",
        "ResponseCode": "0",
        "ErrorCode": "1004",
        "ErrorMessage": "CancelPremium字段不能为空"
    }
}
[2025-02-12 14:52:38]-Request:
{
    "Data": {
        "PolicyRef": "PI07306250225263683839",
        "CancelDate": "20250212145238",
        "CancelFlag": "0"
    },
    "ChannelCode": "O00001",
    "RequestID": "ZIDINGLFW4E3O8KU6HK9BVXUS5UMGVF5",
    "RequestType": "0016",
    "Version": "1.0.0"
}
[2025-02-12 14:52:38]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 250,
    "ResponseBody": {
        "RequestID": "ZIDINGLFW4E3O8KU6HK9BVXUS5UMGVF5",
        "RequestType": "0016",
        "ResponseCode": "1",
        "ErrorCode": "0000",
        "ErrorMessage": "成功",
        "Data": {
            "PolicyRef": "PI07306250225263683839",
            "RefundPremium": "8.29"
        }
    }
}
[2025-02-12 14:52:49]-Request:
{
    "Data": {
        "PolicyRef": "PI07306250225263683839",
        "CancelDate": "20250212145249",
        "CancelPremium": 8.29,
        "Currency": null,
        "Type": null,
        "ReasonRemark": null
    },
    "ChannelCode": "O00001",
    "RequestID": "ZIDINGIFZB9ZR17QE2CWNGIZOA5HPNZ3",
    "RequestType": "0017",
    "Version": "1.0.0"
}
[2025-02-12 14:52:52]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 657,
    "ResponseBody": {
        "RequestID": "ZIDINGIFZB9ZR17QE2CWNGIZOA5HPNZ3",
        "RequestType": "0017",
        "ResponseCode": "0",
        "ErrorCode": "12001",
        "ErrorMessage": "100，保单状态已失效，无法申请退保！错误码:15818"
    }
}
[2025-02-28 14:22:10]-Request:
{
    "Data": {
        "PolicyRef": "PI07306230824779981301",
        "Type": "0",
        "PaymentDate": "20230221000000",
        "Currency": "CNY",
        "PaymentMethod": "2",
        "PaymentFlowNum": "ZIDINGI8FJ20KXWSZHZ6RYOW5ZP249LY",
        "StartInstallmentNo": "4",
        "PaymentPremium": "54.90",
        "DiscountPremium": "0",
        "MerchantOrderNum": null
    },
    "RequestID": "ZIDINGWXQAIQ1IDJHLFXAHSC8II9KEOP",
    "Version": "1.0.0",
    "ChannelCode": "O00001",
    "RequestType": "0035"
}
[2025-02-28 14:22:10]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 213,
    "ResponseBody": {
        "RequestID": "ZIDINGWXQAIQ1IDJHLFXAHSC8II9KEOP",
        "RequestType": "0035",
        "ResponseCode": "0",
        "ErrorCode": "1005",
        "ErrorMessage": "保单号不存在，请确认"
    }
}
[2025-02-28 14:25:53]-Request:
{
    "Data": {
        "PolicyRef": "PI07306230824779981301",
        "Type": "0",
        "PaymentDate": "20230221000000",
        "Currency": "CNY",
        "PaymentMethod": "2",
        "PaymentFlowNum": "ZIDINGTVYSD7QCHB4R44NGUAJN69TNYB",
        "StartInstallmentNo": "4",
        "PaymentPremium": "54.90",
        "DiscountPremium": "0",
        "MerchantOrderNum": null
    },
    "RequestID": "ZIDING0A4UTONSUJNF2AH6DEFSG16WDS",
    "Version": "1.0.0",
    "ChannelCode": "O00001",
    "RequestType": "0035"
}
[2025-02-28 14:25:53]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 158,
    "ResponseBody": {
        "RequestID": "ZIDING0A4UTONSUJNF2AH6DEFSG16WDS",
        "RequestType": "0035",
        "ResponseCode": "0",
        "ErrorCode": "1005",
        "ErrorMessage": "保单号不存在，请确认"
    }
}
[2025-02-28 14:27:31]-Request:
{
    "Data": {
        "PolicyRef": "PI07306230824779981301",
        "Type": "0",
        "PaymentDate": "20230221000000",
        "Currency": "CNY",
        "PaymentMethod": "2",
        "PaymentFlowNum": "ZIDING36K5CSGKNJEY68MVNBCK6HT7QR",
        "StartInstallmentNo": "4",
        "PaymentPremium": "54.90",
        "DiscountPremium": "0",
        "MerchantOrderNum": null
    },
    "RequestID": "ZIDINGAIC37RXJ1X8N19I2GM4ML27ABP",
    "Version": "1.0.0",
    "ChannelCode": "O00001",
    "RequestType": "0035"
}
[2025-02-28 14:27:31]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 205,
    "ResponseBody": {
        "RequestID": "ZIDINGAIC37RXJ1X8N19I2GM4ML27ABP",
        "RequestType": "0035",
        "ResponseCode": "0",
        "ErrorCode": "1005",
        "ErrorMessage": "保单号不存在，请确认"
    }
}
[2025-03-03 09:48:28]-Request:
{
    "Data": {
        "PolicyRef": "PI07306230824779981301",
        "Type": "0",
        "PaymentDate": "20230221000000",
        "Currency": "CNY",
        "PaymentMethod": "2",
        "PaymentFlowNum": "ZIDING1VCXDGQ4VR0PIFSUTK29CTWXG6",
        "StartInstallmentNo": "4",
        "PaymentPremium": "54.90",
        "DiscountPremium": "0",
        "MerchantOrderNum": null
    },
    "RequestID": "ZIDING1IRCIRW8NZ3LDKUBBHWKPSWCTX",
    "Version": "1.0.0",
    "ChannelCode": "O00001",
    "RequestType": "0035"
}
[2025-03-03 09:48:28]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 228,
    "ResponseBody": {
        "RequestID": "ZIDING1IRCIRW8NZ3LDKUBBHWKPSWCTX",
        "RequestType": "0035",
        "ResponseCode": "0",
        "ErrorCode": "1005",
        "ErrorMessage": "保单号不存在，请确认"
    }
}
[2025-03-03 09:56:13]-Request:
{
    "Data": {
        "PolicyRef": "PI07306230824779981301",
        "Type": "0",
        "PaymentDate": "20230221000000",
        "Currency": "CNY",
        "PaymentMethod": "2",
        "PaymentFlowNum": "ZIDING7H2FKZOXB66DZE8UZLIVFFN78U",
        "StartInstallmentNo": "4",
        "PaymentPremium": "54.90",
        "DiscountPremium": "0",
        "MerchantOrderNum": null
    },
    "RequestID": "ZIDING388WG7BQI5F497SSCSNQO4XM7N",
    "Version": "1.0.0",
    "ChannelCode": "O00001",
    "RequestType": "0035"
}
[2025-03-03 09:56:13]-Response:
{
    "StatusCode": 200,
    "ResponseTime": 160,
    "ResponseBody": {
        "RequestID": "ZIDING388WG7BQI5F497SSCSNQO4XM7N",
        "RequestType": "0035",
        "ResponseCode": "0",
        "ErrorCode": "1005",
        "ErrorMessage": "保单号不存在，请确认"
    }
}
