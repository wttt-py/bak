import paho.mqtt.client as mqtt
import json
import time
# MQTT服务器
host = "127.0.0.1"
# 端口
port = 1883
# 主题
topic = "act_k"
# 发布的消息（数据）
# data = bytes([0x80, 0x00, 0x02, 0x00, 0x00, 0x15, 0x00, 0x00, 0x00, 0x10, 0x50,
#               0x10, 0xCC, 0x08, 0xA1, 0x23, 0x0E, 0x01, 0x00, 0x00, 0xC1, 0x00, 0x6F])
# data = json.dumps({'d' : '111'})

# 一旦连接成功，回调此方法（连接成功）
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

# 消息接收回调
def on_message(client, userdata, msg):
    #在这里处理业务逻辑
    print(msg.topic+" "+str(msg.payload))


# def readJsonFileToStr(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         text = f.read()
#         f.close()
#     return text


client = mqtt.Client()
# 指定回调函数
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port, 30)  

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        curLine=line.strip().split("##")
        data = json.dumps({'a':curLine[0], 'b':curLine[1]})
        client.publish(topic, payload=data, qos=0)
        time.sleep(1)
    f.close()



