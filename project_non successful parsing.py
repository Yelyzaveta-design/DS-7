#!/usr/bin/env python
# coding: utf-8

# In[67]:


#pip install lxml


# In[68]:


#pip install requests


# In[69]:


#pip install beautifulsoup4


# In[76]:


import requests 
from bs4 import BeautifulSoup as bs

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

url = 'https://www.google.com.ua/maps/search/%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8+%D0%BC%D0%B5%D1%82%D1%80%D0%BE+%D0%BA%D0%B8%D0%B5%D0%B2+%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D1%8B+/@50.4852635,30.4195925,12z/data=!3m1!4b1?hl=ru'
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
variable = soup.find_all('a')
for tag in variable:
    print(tag.get('href'))


# In[122]:


import requests
import lxml
from bs4 import BeautifulSoup
HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

SITE = 'https://www.google.com.ua/maps/search/%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8+%D0%BC%D0%B5%D1%82%D1%80%D0%BE+%D0%BA%D0%B8%D0%B5%D0%B2+%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D1%8B+/@50.4852635,30.4195925,12z/data=!3m1!4b1?hl=ru'
r = requests.get(SITE, HEADERS)
r.status_code


# In[123]:


for SITE in soup.find_all('a'):
    print(SITE.get('href'))


# In[124]:


soup = BeautifulSoup(r.text, 'lxml')
url = soup.find('a', class_='class="a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd').get('href')


# In[ ]:





# In[112]:


soup = BeautifulSoup(r.text, 'lxml')
product = soup.find('div', class_="jsaction")


# In[118]:


def get_coordinate(html):
    soup=BeautifulSoup(html, 'lxml')
    items=soup.find_all('div', class_='siAUzd-neVct section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc siAUzd-neVct-Q3DXx-BvBYQ')
    
    links=[]
    for i in items:
        links.append(i.a.get('href'))
    l=[]
    for i in links:
        soup=BeautifulSoup(get_html(i).text, 'lxml')
        l.append ((
            soup.find('a', class_='a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd').text.split()[1]
        ))
    return l


# In[97]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[111]:


import re
result = re.findall(r'((\d)(\d).(\d)(\d)(\d)(\d)(\d)(\d)(\d))', 'https://www.google.com.ua/maps/place/%D0%A1%D1%8B%D1%80%D0%B5%D1%86/data=!4m5!3m4!1s0x40d4cdae239e4117:0x293f7a0b259eb3b6!8m2!3d50.4767618!4d30.4327791?authuser=0&hl=ru&rclk=1')
x=result[0]
y=result[1]


# In[ ]:


import re
result = re.findall(r'((\d)(\d).(\d)(\d)(\d)(\d)(\d)(\d)(\d))', 'https://www.google.com.ua/maps/place/%D0%A1%D1%8B%D1%80%D0%B5%D1%86/data=!4m5!3m4!1s0x40d4cdae239e4117:0x293f7a0b259eb3b6!8m2!3d50.4767618!4d30.4327791?authuser=0&hl=ru&rclk=1')
print (result)
let firstMatch = matchAll[0];
alert( firstMatch[0] )


# In[60]:


metro_station = {}
for station in soup.find_all('div', class_="V0h1Ob-haAclf gd9aEe-LQLjdd OPZbO-KE6vqe")[0:20]:
    station = soup.find('a', class_="a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd").text
    link = station.a.get('href')
    metro_station[station] = link


# In[61]:


metro_station


# In[53]:


station = station.find('a', class_="a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd").text


# In[38]:


soup = BeautifulSoup(r.text, 'lxml')
station = soup.find('div', class_="V0h1Ob-haAclf gd9aEe-LQLjdd OPZbO-KE6vqe")


# In[39]:


variable = soup.find_all('a') #получаем вообще все, что связано с тегом a href
for tag in variable: #и теперь по этому списку идем, выгребая конкретно ссылки
print(tag.get('href'))


# In[35]:


import urllib.request
from bs4 import BeautifulSoup
html = urllib.request.urlopen('https://www.google.com.ua/maps/search/%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8+%D0%BC%D0%B5%D1%82%D1%80%D0%BE+%D0%BA%D0%B8%D0%B5%D0%B2+%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D1%8B+/@50.4852635,30.4195925,12z/data=!3m1!4b1?hl=ru')
soup = BeautifulSoup(r.text, 'lxml')
info = soup.find('div', {'class': 'siAUzd-neVct section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc siAUzd-neVct-Q3DXx-BvBYQ'})
for i in info('a', href=True):
    print(i['href'])


# In[24]:


post = []
soup = BeautifulSoup(r.text, 'lxml')
image_links = soup.find_all('div', {'class': 'V0h1Ob-haAclf gd9aEe-LQLjdd OPZbO-KE6vqe'})
for link in image_links:
    link = link.find('a').get('href')
    post.append('link')


# In[25]:


post


# In[ ]:


import re
pattern = re.compile(r'href="(.*)">')
html = urllib.request.urlopen('http://your/url')

<a class="gb_6b gb_Aa gb_Pb" href="https://myaccount.google.com/brandaccounts?authuser=0&amp;continue=https://www.google.com.ua/maps/%4050.4851493,30.4721233,14z%3Fhl%3Dru&amp;service=/maps/preview%3Fauthuser%3D%24authuser" aria-hidden="true"><div class="gb_7b"><svg focusable="false" height="20" viewBox="0 0 24 24" width="20" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 2v10.79C16.52 14.37 13.23 14 12 14s-4.52.37-7 1.79V5h14zM5 19v-.77C6.74 16.66 10.32 16 12 16s5.26.66 7 2.23V19H5zm7-6c1.94 0 3.5-1.56 3.5-3.5S13.94 6 12 6 8.5 7.56 8.5 9.5 10.06 13 12 13zm0-5c.83 0 1.5.67 1.5 1.5S12.83 11 12 11s-1.5-.67-1.5-1.5S11.17 8 12 8z" fill="#5F6368"></path><path d="M0 0h24v24H0V0z" fill="none"></path></svg></div><div class="gb_9b gb_ac">Все аккаунты брендов</div><svg class="gb_bc" focusable="false" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill="#5F6368"></path><path d="M0 0h24v24H0z" fill="none"></path></svg></a>

soup = BeautifulSoup(html, 'html.parser').find('div', class_='First-class')
print(re.findall(pattern, str(soup)))


# In[12]:


link = product.a.get('href')
link


# In[ ]:




