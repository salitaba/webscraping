# import requests

# res = requests.get('https://hls.harvard.edu/faculty/directory/?l=l');

from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio
# import grequests
import requests


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


# driver = webdriver.Firefox()
# driver.get('https://hls.harvard.edu/faculty/directory/?l=l')
# print(driver.find_element_by_class_name("faculty-detail-link"))
# content = driver.page_source
f = open("emails.txt", "a")
res = requests.get(HOST + '/faculty/directory/?l=l')
content = res.content

soup = BeautifulSoup(content)
links = soup.findAll('a', href=True, attrs={'class': 'faculty-detail-link'})
emails = []
for a in soup.findAll('a', href=True, attrs={'class': 'faculty-detail-link'}):
    # name = a.find('div', attrs={'class':'sfljd'})
    try:
        url = a.get('href')
        email = print_mail(url)
        emails.append(email)
        f.write(email + "\n")
    except:
        print("cant read")

print(emails)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()


