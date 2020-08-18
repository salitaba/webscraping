# import requests

# res = requests.get('https://hls.harvard.edu/faculty/directory/?l=l');

from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio
# import grequests
import requests


HOST = 'https://hls.harvard.edu'


def print_mail(url):
    res = requests.get("https://www.hks.harvard.edu"+url)
    content = res.content
    # print(content)
    soup = BeautifulSoup(content)
    url = soup.find('a', attrs={'class': "contact"}).get('href')
    email = url.split(':')
    if (len(email) > 1):
        email = email[1].split('AT')[0] + "@hks.harvard.edu"
        print(email)
        return email
    return ""


# driver = webdriver.Firefox()
# driver.get('https://hls.harvard.edu/faculty/directory/?l=l')
# print(driver.find_element_by_class_name("faculty-detail-link"))
# content = driver.page_source
f = open("hks-harvard.txt", "a")


for i in range(0, 12):
    res = requests.get("https://www.hks.harvard.edu/faculty-directory?search_api_fulltext=&page={0}".format(i))
    content = res.content
    # print(content)
    soup = BeautifulSoup(content)
    divs = soup.findAll('h2', attrs={'class': 'node-title'})
    emails = []
    # print(divs)
    for div in divs:
        # name = a.find('div', attrs={'class':'sfljd'})
        try:
            url = div.find('a').get('href')
            email = print_mail(url)
            emails.append(email)
            f.write(email + "\n")
        except:
            print("cant read")

# print(emails)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()


