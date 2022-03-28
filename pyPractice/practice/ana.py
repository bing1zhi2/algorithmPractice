# coding:utf-8
import os

from kafka import KafkaProducer


def utf8len(s):
    return len(s.encode('utf-8'))


origin_str = "887xxx_"
print(utf8len(origin_str))
sss = origin_str * 262144
# print(sss)
print(utf8len(sss))
# KafkaProducer()
SERVERS = ["192.168.3.22:9094"]
producer = KafkaProducer(bootstrap_servers=SERVERS, max_request_size=5242880)

# msg = json.dumps(msg_dict)
msg = sss.encode(encoding="utf-8")
partition = None

future = producer.send("test", msg, partition=partition)

print("done")