# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:44:29 2021

@author: 读书的爹爹
"""


import requests
from bs4 import BeautifulSoup
import time
mine=[]
gold=[]
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
res=requests.get('https://www.tupianzj.com/meinv/mm/meizitu/',headers=headers)
res.encoding='gb2312'
soup=BeautifulSoup(res.text,'html.parser')
aim=soup.find_all('span',class_="soxflashtext")
for i in aim:
    tag=i.find('a')
    name=tag.text
    link=tag['href']
    
    mine.append(link)
# =============================================================================
# print(mine)
# =============================================================================
# =============================================================================
# =============================================================================
for m in mine[1:]:
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
           }
        resp=requests.get('https://www.tupianzj.com/'+m)
        resp.encoding='gb2312'
        souper=BeautifulSoup(resp.text,'html.parser')
        wasp=souper.find_all('center')
        for i in wasp:
            tag=i.find('img')
            link=tag['src']
            gold.append(link)
        for i in gold:
            img_resp=requests.get(i)
            img_name=i.split('/')[-1]
            with open (img_name,mode='wb')as f:
               f.write(img_resp.content)
            print('over',img_name)
            time.sleep(1)
print('all_over!!')