import pika

params = pika.URLParameters("amqps://iypmhetc:eQRzc9A1dF6GeYjVO3geIGdHkVH9KW17@cow.rmq2.cloudamqp.com/iypmhetc")
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare("main")

def callback(channel, method, propertis, body):
    print("Received in main")
    print(body)

channel.basic_consume("main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()