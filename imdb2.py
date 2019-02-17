from bs4 import BeautifulSoup
import requests


url='https://www.imdb.com/gallery/rg1859820288?ref_=nv_ph_ls'
page=requests.get(url)

soup=BeautifulSoup(page.content,'lxml')

lis=soup.find('div',{'class':'media_index_thumb_list'})

img=lis.find_all('img')
#for img_tag in img:
#   print(img_tag['img'])
#now download one img
f=open('img.jpg','wb')
f.write(requests.get(img[1]['src']).content)
f.close()
