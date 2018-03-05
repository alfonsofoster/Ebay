import logging

def log():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='log_orchestra.log',level=logging.INFO)
    return
