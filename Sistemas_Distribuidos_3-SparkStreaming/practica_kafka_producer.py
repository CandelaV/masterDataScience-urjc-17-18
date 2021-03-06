from kafka import KafkaProducer
import random
from time import sleep
import sys, os

if __name__=="__main__":

    if (len(sys.argv) < 4):
        print("Usage: python practica_kafka_producer.py <low_thres> <high_thres> <topic_name> <data_filename>")
        print("Suggested: python practica_kafka_producer.py 0.4 0.9 test data/DATASET-Twitter-23-26-Mar-2014-MotoGP-Qatar.csv")

    try:
        print("Initialization...")
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
    
        print("Sending messages to kafka 'test' topic...")
        low = sys.argv[1]
        high = sys.argv[2]
        topic = sys.argv[3]
        filename = sys.argv[4]
    
        f = open(filename, 'rt')
        try:
            for line in f:
                print(line)
                producer.send(topic, bytes(line, 'utf8'))
                sleep(random.uniform(float(low), float(high)))
        finally:
            f.close()
    
        print("Waiting to complete delivery...")
        producer.flush()
        print("End")

    except KeyboardInterrupt:
        print('Interrupted from keyboard, shutdown')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
