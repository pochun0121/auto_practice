import logging

class consoleFilter(logging.Filter):
    def filter(self, record):
        # return True means keep this message
        if record.levelno != logging.INFO:
            return False
        if '[TESTCASE]' in record.msg:
            return False
        return True
 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s (%(filename)s:%(lineno)s) [%(levelname)s] %(message)s',
    handlers = [logging.FileHandler('consoleDebug.log', 'w', 'utf-8'),]
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

formatter = logging.Formatter(
    fmt='%(asctime)s [%(name)s] %(message)s',
    datefmt='%H:%M:%S')
console.setFormatter(formatter)
console.addFilter(consoleFilter())
logging.getLogger('').addHandler(console)

def get_logger(name):
    return logging.getLogger(name)
