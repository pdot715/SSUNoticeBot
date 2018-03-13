
import requests
from bs4 import BeautifulSoup
import os
import telegram

bot = telegram.Bot(token='12345678:TesttTestTestTest')
chat_id = 12345678

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://m.ssu.ac.kr/html/themes/m/html/notice_univ_list.jsp')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('li.first-child > a')
address = posts[0].get('href')
latest = posts[0].text

with open(os.path.join(BASE_DIR, 'latest_soongsil.txt'), 'r+') as f_read:
    before = f_read.readline()
    f_read.close()
    if before != latest+address:
        bot.sendMessage(chat_id=chat_id, text='학교 공지사항에 새로운 글')
        bot.sendMessage(chat_id=chat_id, text=latest)
        bot.sendMessage(chat_id=chat_id, text='http://m.ssu.ac.kr'+address)
        with open(os.path.join(BASE_DIR, 'latest_soongsil.txt'), 'w+') as f_write:
            f_write.write(latest)
            f_write.write(address)
            f_write.close()

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
        bot.sendMessage(chat_id=chat_id, text='학부 취업 게시판에 새로운 글')
        bot.sendMessage(chat_id=chat_id, text=latest_cse_job)
        bot.sendMessage(chat_id=chat_id, text='http://cse.ssu.ac.kr/05_sub/05_sub.htm'+address_cse_job)
        with open(os.path.join(BASE_DIR, 'latest_cse_job.txt'), 'w+') as f_write:
            f_write.write(latest_cse_job)
            f_write.write(address_cse_job)
            f_write.close()

req_cse = requests.get('http://cse.ssu.ac.kr/main/index.htm')
req_cse.encoding = 'utf-8'

html_cse = req_cse.text
soup_cse = BeautifulSoup(html_cse, 'html.parser')

posts_cse = soup_cse.select('ul > li > span > a')
address_onclick = posts_cse[0].get('onclick')
# 문자열 자르기로 게시글 숫자만 빼기
address_cse = address_onclick[13:17]
latest_cse = posts_cse[0].text

with open(os.path.join(BASE_DIR, 'latest_cse.txt'), 'r+') as f_read:
    before_cse = f_read.readline()
    f_read.close()
    if before_cse != latest_cse+address_cse:
        bot.sendMessage(chat_id=chat_id, text=latest_cse)
        bot.sendMessage(chat_id=chat_id, text='http://cse.ssu.ac.kr/03_sub/01_sub.htm?no='+address_cse+'&bbs_cmd=view')
        with open(os.path.join(BASE_DIR, 'latest_cse.txt'), 'w+') as f_write:
            f_write.write(latest_cse)
            f_write.write(address_cse)
            f_write.close()
