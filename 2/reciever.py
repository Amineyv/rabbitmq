import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
