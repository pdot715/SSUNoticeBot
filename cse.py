
import requests
from bs4 import BeautifulSoup
import os

import telegram

bot = telegram.Bot(token='12345678:TesttTestTestTest')
chat_id = 12345678

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req_cse = requests.get('http://cse.ssu.ac.kr/03_sub/01_sub.htm')
req_cse.encoding = 'utf-8'

html_cse = req_cse.text
soup_cse = BeautifulSoup(html_cse, 'html.parser')

posts_cse = soup_cse.select('td > a')
address_cse = posts_cse[0].get('href')
latest_cse = posts_cse[0].text

with open(os.path.join(BASE_DIR, 'latest_cse.txt'), 'r+') as f_read:
    before_cse = f_read.readline()
    f_read.close()
    if before_cse != latest_cse+address_cse:
        bot.sendMessage(chat_id=chat_id, text=latest_cse)
        bot.sendMessage(chat_id=chat_id, text='http://cse.ssu.ac.kr/03_sub/01_sub.htm'+address_cse)
        with open(os.path.join(BASE_DIR, 'latest_cse.txt'), 'w+') as f_write:
            f_write.write(latest_cse)
            f_write.write(address_cse)
            f_write.close()


