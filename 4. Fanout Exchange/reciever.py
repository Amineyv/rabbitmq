from threading import ExceptHookArgs
import pika
import time



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

ch = connection.channel()

# you have to declare your exchange. reason: if you open your reciever first, it has to be declared.

ch.exchange_declare(exchange='logs', exchange_type='fanout')

result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

ch.queue_bind(queue=qname, exchange='logs')

print('Waiting for logs.')

def callback(ch,method,properties,body):
    print(f'recieved {body}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=False)

ch.start_consuming()

connection.close()