import json

import pika


params = pika.URLParameters("amqps://iypmhetc:eQRzc9A1dF6GeYjVO3geIGdHkVH9KW17@cow.rmq2.cloudamqp.com/iypmhetc")
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body),properties=properties)