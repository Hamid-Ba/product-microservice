import os, django
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

params = pika.URLParameters("amqps://iypmhetc:eQRzc9A1dF6GeYjVO3geIGdHkVH9KW17@cow.rmq2.cloudamqp.com/iypmhetc")
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare("admin")

def callback(channel, method, propertis, body):
    print("Received in Admin")
    print(body)

channel.basic_consume("admin", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()