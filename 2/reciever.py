import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare('first',durable=True)

def callback(ch, method, properties, body):
    print(f'recieved, {body}')
    print(method)
    time.sleep(9)
    print('Done.')
    # make sure to put this acknowledgement at the end of your code, so if the data is lost in the middle of the process, 
    # the message will not be removed from the list_queue
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

print('Waiting for message, press ctrl+c to exit')

ch.basic_qos(prefetch_count=5)

ch.basic_consume('first', on_message_callback=callback)

ch.start_consuming()

