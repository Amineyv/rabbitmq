 import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare(queue='first'durable=True)

message = 'This is the first testing message.'

ch.basic_publish('','first',message,properties=pika.BasicProperties(delivery_mode=2,))

print('Message sent.')

connection.close()