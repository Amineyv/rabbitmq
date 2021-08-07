import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

ch1 = connection.channel()

ch1.queue_declare(queue="Hello")

ch1.basic_publish(exchange='',routing_key='Hello',body='Hello World.')


print('Message Sent')


connection.close()
