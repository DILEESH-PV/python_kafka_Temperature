import random
import time
from kafka import KafkaProducer

bootstrap_server = ["localhost:9092"]
topic = "home"
producer = KafkaProducer(bootstrap_servers = bootstrap_server)

producer = KafkaProducer()

def senddata():
    temp = random.randint(0,40)
    message = producer.send(topic,bytes(str(temp),"utf-8"))

    metadata = message.get()
    print(metadata.topic)
    print(metadata.partition)
    time.sleep(5)
while True:
    senddata()