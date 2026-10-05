import logging
import allure


def get_logger(name: str):
    return logging.getLogger(name)

def allure_and_logger(text):
    with allure.step(text):
        logger = get_logger(__name__)
        logger.info(text)
