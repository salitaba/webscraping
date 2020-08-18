# import requests

# res = requests.get('https://hls.harvard.edu/faculty/directory/?l=l');

from selenium import webdriver
from bs4 import BeautifulSoup
import asyncio
# import grequests
import requests


HOST = 'https://hls.harvard.edu'


def print_mail(text):
    email = text.split(':')
    if(len(email) > 1):
        print(email[1])
        return email[1]
    return ""


# driver = webdriver.Firefox()
# driver.get('https://hls.harvard.edu/faculty/directory/?l=l')
# print(driver.find_element_by_class_name("faculty-detail-link"))
# content = driver.page_source
f = open("polis.txt", "a")
res = requests.get("https://www.polis.cam.ac.uk/Staff_and_Students/academic-staff")
content = res.content
# print(content)
soup = BeautifulSoup(content)
divs = soup.findAll('div', attrs={'class': 'emailAddress'})
emails = []
# print(divs)
for div in divs:
    # name = a.find('div', attrs={'class':'sfljd'})
    try:
        text = div.find('a').get('href')
        email = print_mail(text)
        emails.append(email)
        f.write(email + "\n")
    except:
        print("cant read")

# print(emails)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()


