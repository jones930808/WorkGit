# -*- coding: utf-8 -*-
# @Author  : WuJiLiu
# @Pseudonym : ToyRocket
# @FileName: yamloperation.py
# @Software: PyCharm
# @Time    : 2025/1/3 11:24
# @Email   : 1151905906@qq.com
import os
import yaml


class YamlOperation:
    def __init__(self, file_path, file_name, is_testcase=False):
        self.file_path = file_path
        self.file_name = file_name
        self.is_testcase = is_testcase
        self.yaml_obj = self.load_yaml(file_path)  # 使用load_yaml方法加载文件

    # 预加载yaml文件,转换为字典或列表
    def load_yaml(self, file_path):
        # 判断yaml文件是否为空
        if not os.path.exists(file_path):  # 文件不存在时抛出错误
            print(f"Error: the file {file_path} does not exist ")
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:  # 加入编码方式，以防跨平台出现问题
                return yaml.safe_load(f) or {}  # 防止返回None，返回空字典
        except Exception as e:
            print(f"Error reading the YAML file: {e}")
            return {}

    # 将预加载的yaml文件内容存储，方便读取
    # 该方法后续需要加入额外内容添加的功能
    def save_yaml(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:  # 用file_path来保存文件
                yaml.dump(self.yaml_obj, f, default_flow_style=False, allow_unicode=True)
                print("YAML file saved successfully")
            return True
        except Exception as e:
            print(f"Error writing the YAML file: {e}")
            return False

    # 根据key获取对应字段信息
    def read_yaml(self, keys, default=None):
        # 读取单个键时，转换为列表
        if isinstance(keys, str):
            keys = [keys]
        value = self.yaml_obj
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key, default)
            else:
                return default  # 如果值不是字典类型，直接返回默认值
        return value

    # 获取文件中的所有顶级键
    def get_all_keys(self):
        return list(self.yaml_obj.keys()) if self.yaml_obj else []


if __name__ == '__main__':
    # 测试代码
    yaml_op = YamlOperation("D:/PythonSE/SminulatedData/IoTDataAuto/config/mqtt_config.yaml", "mqtt_config.yaml")
    vpp01 = yaml_op.read_yaml(("vpp01", "username"))
    print(type(vpp01))
    print(f"vpp01: {vpp01}")
