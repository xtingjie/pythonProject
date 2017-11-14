# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import requests
from bs4 import BeautifulSoup
#h = requests.get('http://www.biqukan.com/1_1094/5403177.html')
#soup = BeautifulSoup(h.content, 'lxml')
#texts = soup.find_all(id='content', class_='showtxt')
#
#b = texts[0].getText()
#
#s = b.replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', "\n")
#
##soup_text = BeautifulSoup(str(texts), 'lxml')
##s = soup_text.div.text.replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0','')
#
#file = open('c.txt', 'w+')
#file.write(s)
#file.close()

#for i in soup.find_all('a'):
#    if i.text=='下一章':
#        print(i.get('href'))




def getNovel(url):
    h = requests.get(url)
    soup = BeautifulSoup(h.content, 'lxml')
    title = soup.find('h1').text
    zhengwen = soup.find(id='content', class_='showtxt').text
    zhengwen = zhengwen.replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', "\n")
    zhengwen = zhengwen.replace('\xa0\xa0', '\n')
    zhengwen = zhengwen.replace('\u3000\u3000', '\n')
    for i in soup.find_all('a'):
        if i.text=='下一章':
            nextUrl = 'http://www.biqukan.com' + i.get('href')
    novel = title + zhengwen+'\n'
    return novel, nextUrl


novel, nextUrl = getNovel('http://www.biqukan.com/1_1094/5403177.html')

count = 1
while(nextUrl!='http://www.biqukan.com/1_1094'):
    file = open('c.txt', 'a')
    file.write(novel)
    print('下载完成'+str(count)+'章')
    count = count+1
    file.close()
    novel, nextUrl = getNovel(nextUrl)








    
    