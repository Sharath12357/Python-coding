import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logging.DEBUG=("Debug messgage")
logging.ERROR=("Error message")
logging.INFO=("infoiormation message")
logging.CRITICAL=("Critical message")
logging.WARNING=("Warning message")