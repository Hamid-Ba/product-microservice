import pika, json, requests

params = pika.URLParameters("amqps://iypmhetc:eQRzc9A1dF6GeYjVO3geIGdHkVH9KW17@cow.rmq2.cloudamqp.com/iypmhetc")
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare("admin")

def callback(channel, method, propertis, body):
    
    crud = propertis.content_type
    
    id = json.loads(body)
    
    if crud == "like_product":
        print("Like Product Message")
        try:
            requests.post(f"http://0.0.0.0:8000/api/products/like/{id}/")
        except:
            print("Product With This Id Does Not Exist")
    
    print("Received in Admin")
    print(propertis.content_type)
    print(json.loads(body))

channel.basic_consume("admin", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()