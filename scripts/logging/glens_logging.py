import os
import gzip
import time
import logging
from scripts.constants import app_configuration
from logging.handlers import RotatingFileHandler

log_handler_name = app_configuration.file_name
log_level = app_configuration.log_level

class GZipRotator:
    def __call__(self, source, dest):
        os.rename(source, dest)
        f_in = open(dest, 'rb')
        f_out = gzip.open("%s.gz" % dest, 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove(dest)

def get_logger():
    """
    Purpose : To create logger 
    :return: logger object.
    """
    debug_formatter = '%(asctime)s - %(levelname)-6s - %(name)s - [%(threadName)5s:%(filename)5s:%(funcName)5s():''%(lineno)s] - %(message)s'
    formatter_string = '%(asctime)s - %(levelname)-6s - %(name)s - %(levelname)3s - %(message)s'

    if log_level.strip().upper() == app_configuration.log_level:
        formatter_string = debug_formatter

    log_file = os.path.join(log_handler_name + "_" + time.strftime("%Y%m%d") + '.log')
    logger = logging.getLogger(log_handler_name)
    hdlr_service = logging.FileHandler(log_file)
    formatter = logging.Formatter(formatter_string
                                  , "%Y-%m-%d %H:%M:%S")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.strip().upper())
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    r_handler = RotatingFileHandler(log_file, maxBytes=100000000,
                                  backupCount=10)
    r_handler.rotator = GZipRotator()
    logger.addHandler(r_handler)
    hdlr_service.setFormatter(formatter)
    logger.addHandler(hdlr_service)
    logger.setLevel(log_level.strip().upper())
    return logger


logger = get_logger()