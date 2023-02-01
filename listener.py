import multiprocessing
import pika
import yaml
import conf


def on_message(out_file=None):
  def on_message_callback(ch, method, properties, body):
    message = " [x] recieved %s \n" % body.decode("utf-8")
    if out_file is None:
      print(message)
    else:
      out_file.write(message)
  
  return on_message_callback


def start_consuming(ch, queue, callback, auto_ack):
  ch.basic_consume(queue=queue, on_message_callback=callback, auto_ack=auto_ack)
  print(" [*] Waiting for messages in queue %s. To exit press CTRL+C" % queue)
  try:
    ch.start_consuming()
  except KeyboardInterrupt:
    print(" [x] Closing connection... ")


def run_listener(params, queue_name, out_filename):
  with pika.BlockingConnection(params) as connection:
      with connection.channel() as channel:
        with open(out_filename, "a") as out_file:
          start_consuming(channel, queue_name, on_message(out_file), True)


def main():
  config = conf.read()
  credentials = pika.PlainCredentials(config["user"], config["pass"])
  params = pika.ConnectionParameters(
    host=config["addr"],
    port=config["port"],
    credentials=credentials
  )

  listeners = []
  for queue in config["queues"]:
    p = multiprocessing.Process(target=run_listener, args=(params, queue["name"], queue["out"]))
    p.start()
    listeners.append(p)
  
  for p in listeners:
    p.join()


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print(" [x] Finishing... ")
