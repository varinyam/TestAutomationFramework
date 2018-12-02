from selenium import webdriver
import logging
from logging import config

class log():

    def testlog(self):
        logging.config.fileConfig('logging.conf')
        logger =logging.getLogger(log.__name__)

        logger.debug("from debug")
        logger.warning("from warinig")
        logger.error("from error")

lg = log()
lg.testlog()