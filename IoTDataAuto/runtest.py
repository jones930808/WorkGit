# -*- coding: utf-8 -*-
# @Author  : WuJiLiu
# @Pseudonym : ToyRocket 
# @FileName: runtest.py
# @Software: PyCharm
# @Time    : 2025/1/3 15:29
# @Email   : 1151905906@qq.com

from core.mqtt_client import MqttClient
from until.yamloperation import YamlOperation
import time


if __name__ == '__main__':
    file_path = "D:/PythonSE/SminulatedData/IoTDataAuto/config/mqtt_config.yaml"
    file_name = "mqtt_config.yaml"
    yaml_op = YamlOperation(file_path, file_name)
    host = yaml_op.read_yaml(("vpp01", "host"))
    port = yaml_op.read_yaml(("vpp01", "port"))
    username = yaml_op.read_yaml(("vpp01", "username"))
    password = yaml_op.read_yaml(("vpp01", "password"))
    client_id = yaml_op.read_yaml(("vpp01", "client_id"))
    subscribe = yaml_op.read_yaml(("vpp01", "topic_subscribe"))
    publish = yaml_op.read_yaml(("vpp01", "topic_publish"))
    print(type(username))
    print(f"Username: {username}, Port: {port}")

    mqtt_client = MqttClient(host, port, username, password, client_id, subscribe, publish)
    mqtt_client.start()
    mqtt_client.subscribe()
    while True:
        time.sleep(10)

    mqtt_client.stop()
