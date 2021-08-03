import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

ch1 = connection.channel()

ch1.queue_declare(queue="Hello")

ch1.basic_publish()
