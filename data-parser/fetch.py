import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

for i in range(4, 82):
    # Create a fake user agent
    user_agent = UserAgent()
    cl = 0
    if i >= 10:
        cl = i
    else:
        cl = "0" + str(i)

    url = f'http://grades.hs.ntnu.edu.tw/classtable/down.asp?sqlstr=15{cl}&type=class&selArrange=L&selWindow=Left'

    headers = {
        "Host": "grades.hs.ntnu.edu.tw",
        "User-Agent": user_agent.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://duckduckgo.com/",
        "Connection": "keep-alive",
        "Cookie": "selWindow=Left; selArrange=L; ASPSESSIONIDSSDQDDQC=BMJFDMPCNHEGGHHIGBEGOEED",
        "Upgrade-Insecure-Requests": "1",
        "Sec-GPC": "1",
        "Cache-Control": "max-age=0"
    }
    resp = requests.get(url , headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')

    sel = soup.select("body form table")

    print(sel)