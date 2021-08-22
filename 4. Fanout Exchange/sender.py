import pika
import time



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')

ch.basic_publish(exchange='logs',routing_key='',body='Testing fanout exchange.')

print('Message sent.')

connection.close()