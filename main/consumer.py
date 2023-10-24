from DTOs.products import ProductDTO
import pika, json, requests

params = pika.URLParameters("amqps://iypmhetc:eQRzc9A1dF6GeYjVO3geIGdHkVH9KW17@cow.rmq2.cloudamqp.com/iypmhetc")
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare("main")

def callback(channel, method, propertis, body):
    crud = propertis.content_type
    
    data = json.loads(body)
    
    if crud == "create_product":
        print("Product Created at main")
        product = ProductDTO(id=data["id"], title=data["title"], image=data["image"])
        requests.post("http://0.0.0.0:8001/products/",json=product.model_dump())
        
    
    elif crud == "update_product":
        print("Product Updated at main")
        product = ProductDTO(id=data["id"], title=data["title"], image=data["image"])
        requests.put(f"http://0.0.0.0:8001/products/{product.id}",json=product.model_dump())
        
    
    elif crud == "delete_product":  
        print("Product Deleted at main")
        requests.delete(f"http://0.0.0.0:8001/products/{data}")
    
    print("Received in main")
    print(body)

channel.basic_consume("main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()