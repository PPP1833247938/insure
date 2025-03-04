# -*- coding: utf-8 -*-
import requests, json, logging
from Manual_Testing.common.encryption_decryption import AesDensity
from Manual_Testing.common.communal import JsonFormatting
from Manual_Testing.common.operation_config import Config
from Manual_Testing.Environment import Environment
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError

# 配置文件
config = Config("config.ini")
# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PrePose:
    def __init__(self):
        """
        初始化方法，从配置中加载相关参数。
        参数:
            Environment: 环境标识，用于获取配置。
        """
        self.Environment = Environment
        try:
            # 加载配置
            self.host = config.get_value(self.Environment, "host")
            self.ChannelCode = config.get_value(self.Environment, "ChannelCode")
            self.key = config.get_value(self.Environment, "key")
            # 解析 headers
            headers_str = config.get_value(self.Environment, "headers")
            if headers_str:
                try:
                    self.headers = json.loads(headers_str)
                except JSONDecodeError as e:
                    logger.error(f"获取headers信息 JSON 解析失败: {e}")
                    self.headers = {}  # 设置为空字典作为默认值
            else:
                self.headers = {}  # 设置为空字典作为默认值
        except Exception as e:
            logger.error(f"初始化配置失败: {e}")
            raise  # 可以选择抛出异常或处理异常


class SendMethod:
    @staticmethod
    def Get(url, params=None, headers=None, timeout=10):
        """
        发送 GET 请求，并返回响应结果。
        参数:
            url (str): 请求的 URL。
            params (dict): 请求参数，默认为 None。
            headers (dict): 请求头，默认为 None。
            timeout (int): 请求超时时间，默认为 10 秒。
        返回:
            dict: 包含状态码、响应时间和响应体的字典。
                  如果发生错误，返回包含错误信息的字典。
        """
        result = {
            "StatusCode": None,
            "ResponseTime": None,
            "ResponseBody": None
        }
        try:
            if not url:
                raise ValueError("URL 不能为空")
            # 发送 GET 请求
            response = requests.get(url=url, params=params, headers=headers, timeout=timeout)
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int(response.elapsed.microseconds / 1000)
            # 尝试解析响应体为 JSON
            try:
                result["ResponseBody"] = response.json()
            except JSONDecodeError:
                result["ResponseBody"] = response.text
            return JsonFormatting(result)
        except ValueError as e:
            result["ResponseBody"] = f"参数错误: {str(e)}"
            return JsonFormatting(result)
        except RequestException as e:
            result["ResponseBody"] = f"请求失败: {str(e)}"
            return JsonFormatting(result)
        except Exception as e:
            result["ResponseBody"] = f"未知错误: {str(e)}"
            return JsonFormatting(result)

    @staticmethod
    def Post_DataJson(url, data=None, headers=None, json=None):
        """
        发送 POST 请求，支持 JSON 和表单数据格式。
        参数:
            url (str): 请求的 URL。
            data (dict): 要发送的表单数据，默认为 None。
            json (dict): 要发送的 JSON 数据，默认为 None。
            headers (dict): 请求头，默认为 None。
        返回:
            dict: 包含状态码、响应时间和响应体的字典。
                  如果发生错误，返回包含错误信息的字典。
        """
        result = {
            "StatusCode": None,
            "ResponseTime": None,
            "ResponseBody": None
        }
        try:
            if not url:
                raise ValueError("URL 不能为空")
            # 发送 POST 请求
            response = requests.post(url=url, data=data, json=json, headers=headers, timeout=10)
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int(response.elapsed.microseconds / 1000)
            # 尝试解析响应体为 JSON
            try:
                result["ResponseBody"] = response.json()
            except JSONDecodeError:
                result["ResponseBody"] = response.text
            return JsonFormatting(result)
        except ValueError as e:
            result["ResponseBody"] = f"参数错误: {str(e)}"
            return JsonFormatting(result)
        except RequestException as e:
            result["ResponseBody"] = f"请求失败: {str(e)}"
            return JsonFormatting(result)
        except Exception as e:
            result["ResponseBody"] = f"未知错误: {str(e)}"
            return JsonFormatting(result)

    @staticmethod
    def PostData_aes(key, url, data=None, headers=None):
        """
        使用 AES 加密发送 POST 请求，并处理响应。
        参数:
            key (str): AES 加密密钥。
            url (str): 请求的 URL。
            data (dict): 要发送的数据，默认为 None。
            headers (dict): 请求头，默认为 None。
        返回:
            dict: 包含状态码、响应时间和响应体的字典。
                  如果发生错误，返回包含错误信息的字典。
        """
        result = {
            "StatusCode": None,
            "ResponseTime": None,
            "ResponseBody": None
        }
        try:
            # 校验输入参数
            if not key or not url:
                raise ValueError("密钥或 URL 不能为空")
            # 初始化 AES 加密工具
            aes = AesDensity(key)
            # 加密数据
            if data is not None:
                encrypted_data = aes.encrypt(json.dumps(data, ensure_ascii=False))
            else:
                encrypted_data = None
            # 发送 POST 请求
            response = requests.post(url=url, data=encrypted_data, headers=headers, timeout=10)
            result["StatusCode"] = response.status_code
            result["ResponseTime"] = int(response.elapsed.microseconds / 1000)
            # 处理响应
            if response.status_code == 200:
                result["ResponseBody"] = json.loads(aes.decrypt(response.text))
            else:
                try:
                    result["ResponseBody"] = json.loads(response.text)
                except JSONDecodeError:
                    result["ResponseBody"] = response.text
            # 格式化结果
            return JsonFormatting(result)
        except RequestException as e:
            result["ResponseBody"] = f"请求失败: {str(e)}"
            return JsonFormatting(result)
        except JSONDecodeError as e:
            result["ResponseBody"] = f"JSON 解析失败: {str(e)}"
            return JsonFormatting(result)
        except ValueError as e:
            result["ResponseBody"] = f"参数错误: {str(e)}"
            return JsonFormatting(result)
        except Exception as e:
            result["ResponseBody"] = f"未知错误: {str(e)}"
            return JsonFormatting(result)


if __name__ == '__main__':
    """
    """
