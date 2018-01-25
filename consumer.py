#!/usr/bin/env python

import pika
import time
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("10.10.10.3",
                          credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange="hello-exchange",
                         exchange_type="direct",
                         passive=False,
                         durable=True,
                         auto_delete=False)
channel.queue_declare(queue="hello-queue")
channel.queue_bind(queue="hello-queue",
                   exchange="hello-exchange",
                   routing_key="hola")
def msg_consumer(channel, method, header, body):
  channel.basic_ack(delivery_tag=method.delivery_tag)
  #if body == "quit":
  #  channel.basic_cancel(consumer_tag="hello-consumer")
  #  channel.stop_consuming()
  #else:
  #  print body
  #  time.sleep(len(body))
  try:
    print "Received: " + body
    time.sleep(int(body))
    print "woke up"
  except TypeError:
    print "ERROR: cannot convert message to int"
  return
channel.basic_consume( msg_consumer,
                       queue="hello-queue",
                       consumer_tag="hello-consumer")
channel.start_consuming()
