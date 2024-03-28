from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import re

WINDOW_SIZE = '1920,1080'
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


def gen_text(theme):
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get('https://ya.ru/alisa_davay_pridumaem')
        sleep(3)

        text_input = browser.find_element(By.CLASS_NAME, 'input-container__text-input')
        text_input.send_keys(f'напиши актуальный вопрос про {theme}')
        text_input.send_keys(Keys.ENTER)
        sleep(5)

        message = browser.find_elements(By.CLASS_NAME, 'message-bubble')[-1]

        text_input.send_keys('2 предложения про ' + message.text)
        text_input.send_keys(Keys.ENTER)
        sleep(30)

        message = browser.find_elements(By.CLASS_NAME, 'message-bubble')[-1]

        return message.text


if __name__ == '__main__':
    # print(get_text_y3('чай'))
    ...