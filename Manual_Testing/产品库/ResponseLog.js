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
