from kafka import KafkaConsumer, TopicPartition
from json import loads
import numpy as np
import time
import pickle
import os
import logging


def decode_json(jsons_comb):

    x_train = loads(jsons_comb[0])
    y_train = loads(jsons_comb[1])

    return x_train, y_train

def get_data_from_kafka(**kwargs):

    consumer = KafkaConsumer(
        kwargs['topic'],                                # specify topic to consume from
        bootstrap_servers=[kwargs['client']],
        auto_offset_reset='earliest',                   # automatically reset the offset to the earliest offset (should the current offset be deleted or anything)
        enable_auto_commit=True,                        # offsets are committed automatically by the consumer
        )


    logging.info('Consumer constructed')

    try:

        for message in consumer:
            message = message.value.decode('utf-8')
            os.system(f"echo {message} >> kafka_log1.csv")

    except Exception as e:
        print(e)
        logging.info('Error: '+e)

def load_data(**kwargs):

    # Load the Kafka-fetched data that is stored in the to_use_for_model_update folder

    for file_d in os.listdir(os.getcwd()+kwargs['path_new_data']):

        if 'new_samples.p' in file_d:

            new_samples = pickle.load(open(os.getcwd()+kwargs['path_new_data'] + file_d, "rb"))
            test_set = pickle.load(open(os.getcwd()+kwargs['path_test_set'], "rb"))

            logging.info('data loaded')

            return [new_samples, test_set]

        else:
            logging.info('no data found')



