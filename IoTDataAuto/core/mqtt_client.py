# -*- coding: utf-8 -*-
# @Author  : WuJiLiu
# @Pseudonym : ToyRocket 
# @FileName: mqtt_client.py
# @Software: PyCharm
# @Time    : 2025/1/3 9:59
# @Email   : 1151905906@qq.com
import threading
import paho.mqtt.client as mqtt
import json
import time

class MqttClient:
    # 初始化MQTT客户端连接到指定的mqtt broker
    def __init__(self, host, port, username, password, client_id, topic_subscribe, topic_publish):
        # 创建一个mqtt客户端实例
        self.client = mqtt.Client(client_id)
        # 设置回调函数
        self.client.on_message = self.on_message
        # 设置用户名和密码
        print(f"Username before passing to username_pw_set: {username}, Type: {type(username)}")
        self.client.username_pw_set(username, password)
        # 连接到指定mqtt broker
        self.client.connect(host, port)
        #  订阅主题
        self.topic_subscribe = topic_subscribe
        #  指令下发topic
        self.topic_publish = topic_publish
        # 设置定时停止的时间
        self.stop_time_seconds = self.stop_time_seconds
    # MQTT订阅服务
    def subscribe(self):
        # 订阅指定的topic主题
        self.client.subscribe(self.topic_subscribe)

    # MQTT指令下发
    def publish(self, message):
        # 指定topic进行指令下发
        self.client.publish(self.topic_publish, message)

    # 开启客户端
    def start(self):
        # 启用mqtt客户端连接，创建一个线程，用于与mqtt broker的通信
        self.client.loop_start()

    # 关闭客户端
    def stop(self):
        # 停止mqtt客户端连接，停止事件循环释放资源
        self.client.loop_stop()

    # 回调函数
    def on_message(self, client, userdata, msg):
        # 处理接收到的消息
        try:
            message = json.loads(msg.payload.decode())  # 将消息转换为字典
            print(f"Received message: {message} on topic: {msg.topic}")
        except json.JSONDecodeError:
            print("Received non-JSON message:", msg.payload.decode())

    def stop_after_timeout(self):
        """定时停止监听"""
        print(f"Waiting for {self.stop_time_seconds} seconds before stopping...")
        # 使用 threading.Timer 来设置定时任务
        timer = threading.Timer(self.stop_time_seconds, self.stop_client)
        timer.start()

    def stop_client(self):
        """停止客户端"""
        print("Time is up! Stopping the MQTT client...")
        self.client.loop_stop()  # 停止监听
        self.client.disconnect()  # 断开连接