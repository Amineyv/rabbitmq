import pika
from pika import connection
from pika.spec import Channel

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = ch.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = ('info','warning','error')

for severity in severities:
    ch.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit, press ctrl+C')

def callback(ch, method, properties, body):
    print(f'[*] {method.routing_key}, {body}')

ch.basic_consume(queue=queue_name,on_message_callback=callback, auto_ack=True)

ch.start_consuming()