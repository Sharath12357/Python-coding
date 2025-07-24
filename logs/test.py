from logger import logging

def add(a,b):
    logging.DEBUG=("The addition is taking place")
    return a+b

logging.DEBUG=("The addition is completed")
add(10,2)