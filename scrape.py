import bs4
import requests
res = requests.get('https://en.m.wikipedia.org/wiki/Android_(operating_system)')
type(res)
soup = bs4.BeautifulSoup(res.text, 'lxml')
type(soup)
soup.select('.mf-section-0')
for i in soup.select('.mf-section-0'):
    print(i.text)