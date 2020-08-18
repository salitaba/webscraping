# import requests

# res = requests.get('https://hls.harvard.edu/faculty/directory/?l=l');

from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio
# import grequests
# import requests
import urllib.request as requests
import json


HOST = 'https://law.stanford.edu/directory'


def print_mail(url):
    now_content = requests.get(HOST + url).content
    now_soup = BeautifulSoup(now_content)
    email = now_soup.find('span', attrs={'class': 'email'}).a.get('href')
    email = email.split(':')
    if(len(email) > 1):
        print(email[1])
        return email[1]
    return ""


# driver = webdriver.Firefox()
# driver.get('https://hls.harvard.edu/faculty/directory/?l=l')
# print(driver.find_element_by_class_name("faculty-detail-link"))
# content = driver.page_source
f = open("humand_stanford.txt", "a")


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.11 (KHTML, like Gecko) '
            'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
for i in range(1,9):
    url = "https://profiles.stanford.edu/proxy/api/cap/orgs/school-of-humanities-and-sciences/profiles?p={0}&org=school-of-humanities-and-sciences%2Fsocial-sciences%2Fpolitical-science&affiliations=capFaculty".format(i)
    req = requests.Request(url,headers=headers)
    res = requests.urlopen(req)
    res = res.read()
    # print(url)
    # content = res.content
    # print(content)
    loaded_json = json.loads(res)
    persons = loaded_json['ui']['browseMatches']
    # print(persons)
    for person in persons:
        try:
            f.write(person['email'] + '\n')
            print(person['email'])
        except:
            pass
    # soup = BeautifulSoup(content)
    # print(soup.decode())
    # links = [a.get('href') for a in soup.findAll(
        # 'a', href=True, attrs={'class': 'anchor'})]
    # print(links)
# emails = []
# for a in soup.findAll('a', href=True, attrs={'class': 'faculty-detail-link'}):
#     # name = a.find('div', attrs={'class':'sfljd'})
#     try:
#         url = a.get('href')
#         email = print_mail(url)
#         emails.append(email)
#         f.write(email + "\n")
#     except:
#         print("cant read")

# print(emails)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
