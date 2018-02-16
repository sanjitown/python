from bs4 import BeautifulSoup
import requests
import threading
def photograb(url,string):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    print(soup)
    # imgs=soup.select('img')
    # for img in imgs:
    #     data={
    #         'img':img.get('zoomfile')
    #     }
    #     print(img.get('zoomfile'))

url='https://www.jkforum.net/forum.php?mod=viewthread&tid=8549182&extra=&ordertype=1&threads=thread'
string = 'G:\photo\\1.jpg'
ur='http://diao.ml'
photograb(ur,string)
