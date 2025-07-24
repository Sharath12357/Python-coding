import logging

#Create a logger module 1
logger1=logging.getLogger('module 1')
logger1.setLevel(logging.DEBUG)

# create a logger module 2

logger2=logging.getLogger('module 2')
logger2.setLevel(logging.WARNING)

#Configure logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


logger1.debug=("This is debug message for module 1")
logger2.warning("This is warning message for module 2")
logger2.error("This is error messgae ")