
import requests
from bs4 import BeautifulSoup
import os

import telegram

bot = telegram.Bot(token='12345678:TesttTestTestTest')
chat_id = 12345678

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req_cse_job = requests.get('http://cse.ssu.ac.kr/05_sub/05_sub.htm')
req_cse_job.encoding = 'utf-8'

html_cse_job = req_cse_job.text
soup_cse_job = BeautifulSoup(html_cse_job, 'html.parser')
posts_cse_job = soup_cse_job.select('tr > td > a')
address_cse_job = posts_cse_job[0].get('href')
latest_cse_job = posts_cse_job[0].text

with open(os.path.join(BASE_DIR, 'latest_cse_job.txt'), 'r+') as f_read:
    before_cse_job = f_read.readline()
    f_read.close()
    if before_cse_job != latest_cse_job+address_cse_job:
        bot.sendMessage(chat_id=chat_id, text=latest_cse_job)
        bot.sendMessage(chat_id=chat_id, text='http://cse.ssu.ac.kr/05_sub/05_sub.htm'+address_cse_job)
        with open(os.path.join(BASE_DIR, 'latest_cse_job.txt'), 'w+') as f_write:
            f_write.write(latest_cse_job)
            f_write.write(address_cse_job)
            f_write.close()
    else:  # 원래는 이 메시지를 보낼 필요가 없지만, 테스트 할 때는 봇이 동작하는지 확인차 넣어봤어요.
        bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')


