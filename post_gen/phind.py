from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import re

WINDOW_SIZE = '1920,1080'
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


def gen_ans2text(ans):
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get('https://www.phind.com/agent?home=true')
        sleep(3)

        text_area = browser.find_element(By.CLASS_NAME, 'searchbox-textarea')
        text_area.send_keys(f'напиши пост в канал в пару предложений про {ans} и оберни его в скобки')
        text_area.send_keys(Keys.ENTER)
        sleep(10)

        text = browser.find_element(By.NAME, 'answer-1').text
        return text[text.find('(') + 1:text.rfind(')')]


def gen_text(theme):
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get('https://www.phind.com/agent?home=true')
        sleep(3)

        text_area = browser.find_element(By.CLASS_NAME, 'searchbox-textarea')
        text_area.send_keys(f'напиши вопрос про {theme}')
        text_area.send_keys(Keys.ENTER)
        sleep(5)

        question = browser.find_element(By.NAME, 'answer-1').text
        question = question[question.find('\n') + 1:]

    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get('https://www.phind.com/agent?home=true')
        sleep(3)

        text_area = browser.find_element(By.CLASS_NAME, 'searchbox-textarea')
        text_area.send_keys(question + 'ответь не сложно и кратко в парупредложений')
        text_area.send_keys(Keys.ENTER)
        sleep(30)

        text = browser.find_element(By.NAME, 'answer-1').text
        phind_title = text.find('\n')

        text = text[phind_title + 1:1024 + phind_title - 1]
    print(text)
    return text


if __name__ == '__main__':
    print(gen_ans2text('чай'))
