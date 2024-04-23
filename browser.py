from selenium import webdriver
import logging


def create_browser():
    logging.info('Initilizing Selenium Driver...')
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    return webdriver.Chrome(options)
