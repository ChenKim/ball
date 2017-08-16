import random
import urllib
import re


def get_html(url):
    source = urllib.urlopen(url)
    html = source.read()
    # html = gzip.open(html)
    html = html.decode('utf-8')
    return html


def get_ball(html):
    reg_all = r'<p id="zj_area">([\s\S]*?)</p>'
    reg_red = r'<span class="red_ball">([0-9]+)</span>'
    reg_blue = r'<span class="blue_ball">([0-9]+)</span>'
    ball_list = re.findall(reg_all, html)
    red_ball = re.findall(reg_red, ball_list[0])
    blue_ball = re.findall(reg_blue, ball_list[0])
    red_ball.extend(blue_ball)
    red_ball = map(str, red_ball)
    return red_ball


def get_history(html):
    reg_ball = r'<tr>([\s\S]*?)<td><strong>'
    history_list = re.findall(reg_ball, html)
    reg_date = r'<td align[\s\S]*(\d{4}-\d{2}-\d{2})</td>'
    reg_red = r'<em class="rr">([0-9]+)</em>'
    reg_blue = r'<em>([0-9]+)</em></td>'
    all_data = []

    for item in history_list:
        date = re.findall(reg_date, item)
        date = map(str, date)
        red_ball = re.findall(reg_red, item)
        blue_ball = re.findall(reg_blue, item)
        red_ball.extend(blue_ball)
        red_ball = map(str, red_ball)
        date.extend(red_ball)
        all_data.append(date)
    for item in all_data:
        print item


def gen_ball():
    red_list = []
    while len(red_list) != 6:
        number = random.choice([ball for ball in range(1, 34)])
        if number not in red_list:
            red_list.append(number)
    red_list.sort()
    red_list = map(str, red_list)
    blue = random.choice([ball for ball in range(1, 17)])
    print ', '.join(red_list), "  ", blue

gen_ball()
for i in range(1, 20):
    # trend_html = getHtml('http://trend.caipiao.163.com/ssq/')
    link = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_"+str(i)+".html"
    page = get_html(link)
    get_history(page)
