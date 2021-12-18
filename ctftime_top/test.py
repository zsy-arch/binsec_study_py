import re
import openpyxl
import requests
import bs4


class Contest:
    def __init__(self, name='', score=0.0, link=''):
        self.name = name
        self.score = score
        self.link = link


def get_header(i: int):
    h = {
        "accept": "image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Microsoft Edge\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://ctftime.org/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    return h


rc = re.compile(r'Avg weight: (\d+\.\d+)')


def parse_html(html):
    contests = list()
    sp = bs4.BeautifulSoup(html, features='html.parser')
    ctf_list = sp.find_all('div')
    for tag in ctf_list:
        tag_class = tag.get('class')
        if tag_class is not None and 'thumbnail' in tag_class:
            name_a = tag.find('div').find('h3').find('a')
            if tag.find('div') is None or tag.find('div').find('h3') is None or name_a is None:
                continue
            name = name_a.text
            print(name)
            p_tag = tag.find_all('p')[0]
            text = p_tag.text
            if p_tag is None:
                continue
            if p_tag.a is None:
                continue
            href = p_tag.a.get('href')
            print(href)
            avg = rc.findall(text)
            if avg is None:
                continue
            print(f"found avg: {float(avg[0])}")
            contests.append((name, float(avg[0]), href))
    print('ok')
    return contests


contests = []

i = 1
while True:
    r = requests.request(url=f'https://ctftime.org/ctfs?page={i}', method='GET', headers=get_header(i))
    if not r.status_code == 200:
        break
    print(f'found page: {i}')
    contests += parse_html(r.text)
    i += 1

wb = openpyxl.Workbook()
wb.create_sheet('1')
sheet1 = wb['1']
j = 1
for c in contests:
    sheet1[f'A{j}'] = c[0]
    sheet1[f'B{j}'] = c[1]
    sheet1[f'C{j}'] = c[2]
    # print(str(c[0]) + str(c[1]) + str(c[2]))
    j += 1
wb.save('./out.xlsx')
print(i)
