import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch2 = connection.channel()

ch2.queue_declare(queue='Hello')

def call_back(ch,method,properties,body):
    print(f'Recieved {body}')
    pass

ch2.basic_consume(queue='Hello', on_message_callback=call_back,auto_ack=True)

print('Waiting for message. To exit, please press ctrl+C')

ch2.start_consuming()