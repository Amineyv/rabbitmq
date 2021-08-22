import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

ch = connection.channel()

ch.exchange_declare('direct_logs','direct')

message = {
    'info':'This is the information.',
    'error':'This is the error.',
    'warning':'This is a warning.',
}

print('Message sent.')
for k,v in message.items():
    ch.basic_publish(exchange='direct_logs',routing_key=k,body=v)

connection.close()