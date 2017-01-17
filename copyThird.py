#!/bin/Python
"""
Logging in Python
"""
import logging

def firstLog():
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        logger.info('Start reading database')
        #read database here
        records = {'John':55, 'tom':66}
        logger.debug('Records:%s', records)
        logger.info('Updating records....')
        #update records here
        logger.info('Finish updating records')

def secondLog():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        # Create a file Handler
        handler = logging.FileHandler('hello.log')
        handler.setLevel(logging.INFO)

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.info('Hello baby')

def main():
        secondLog()

if __name__ == '__main__':
        main()




