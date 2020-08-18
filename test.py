from selenium import webdriver
from bs4 import BeautifulSoup
import grequests


rs = (grequests.get(u) for u in urls)

for a in grequests.map(rs):
    print(a)


    # import requests

# res = requests.get('https://hls.harvard.edu/faculty/directory/?l=l');




HOST = 'https://hls.harvard.edu'


def print_mail(url):
    now_content = requests.get(HOST + url).content
    now_soup = BeautifulSoup(now_content)
    email = now_soup.find('span', attrs={'class': 'email'}).a.get('href')
    email = email.split(':')
    if(len(email) > 1):
        print(email[1])
        return email[1]
    return ""


f = open("emails.txt", "a")
res = requests.get(HOST + '/faculty/directory/?l=l')
content = res.content

soup = BeautifulSoup(content)
links = soup.findAll('a', href=True, attrs={'class': 'faculty-detail-link'})
emails = []
reqs = []
for a in soup.findAll('a', href=True, attrs={'class': 'faculty-detail-link'}):
    # name = a.find('div', attrs={'class':'sfljd'})
    url = a.get('href')
    reqs.append(grequests.get(HOST + url))


for res in grequests.map((x for x in reqs))
email = print_mail(url)
emails.append(email)
f.write(email + "\n")
print(emails)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()


