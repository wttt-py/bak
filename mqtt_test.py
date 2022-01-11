import json
import sys
import time
import random
import threading
import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='mqtt_test.log',
                    filemode='w',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

# MQTT服务器
host = "ip"
# 端口
port = 1883
# 主题，alone
topic = "mqtt/push"
# 客户端前缀
cl = 'wttest'
# 客户端数量
client_num = 10
# 每个客户端发送数据条数
push_num = 1000
# 消息发送延迟/秒
delay = 0.1
# 主题锁对应的客户端所属组，all，例:wttest-1-1
topic_group = {"tp1": 1,
               "tp2": 2,
               "tp3": 3}

thread_list = list()
all_data = list()

def mock_data():
    """返回mock数据，调整数据格式"""
    return json.dumps({'a': 'test',
                       'b': random.randint(0, 185),
                       'ts': time.time()})


# # 一旦连接成功，回调此方法
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code: " + str(rc))


def mqtt_client(tag, g, pool):
    """
    mqtt client创建,
    tag:指定数量
    g: 机器所属组
    pool: 客户端连接池
    """
    for i in range(tag):
        cl_name = cl + "--%s--" % g + "%s" % i
        client = mqtt.Client(cl_name)
        try:
            client.connect(host, port, 30)
        except Exception as e:
            logging.error(e)
            logging.error("connect fail to %s" % host)
            sys.exit(1)
        else:
            # client.on_connect = on_connect
            pool.append(client)
            # client.loop_forever()


def push(t, p, g):
    """
    t: topic
    p: 每个客户端发送数据条数
    g: 机器所属组(str--int--int标签的机器)
    """
    log_num, actual = 0, push_num
    pool = list()
    mqtt_client(client_num, g, pool)

    while p != 0:
        for client in pool:
            data = mock_data()
            try:
                client.publish(t, payload=data, qos=0)
            except Exception as e:
                logging.error(e)
                logging.error("The data %s send error" % data)
            else:
                log_num += 1
        time.sleep(delay)
        p -= 1
    if client_num * push_num == log_num:
        logging.info("%s load data %s, test finish;" \
                 % (t, log_num))
        all_data.append(log_num)
    else:
        logging.error('plase check the data ,%s and %s is not equal;' \
                      % (client_num * push_num, log_num))


def topic_push_alone():
    """多个客户端往一个topic推送"""
    return push(topic, push_num, 1)



def topic_push_all():
    """多个客户端并发往多个topic推送"""
    for t, g in topic_group.items():
        thread = threading.Thread(target=push, args=(t, push_num, g))
        thread_list.append(thread)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    logging.info("sum of all data is %s" % sum(all_data))


if __name__ == '__main__':
    # topic_push_alone()
    topic_push_all()
