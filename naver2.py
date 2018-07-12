#-*- coding: utf-8 -*-

import urllib
import requests
from progress.bar import Bar
from bs4 import BeautifulSoup
from datetime import datetime

total_data=[]
titleUrlList=[]
titleList=[]
priceList=[]
dateList=[]
dataSetList=''
editData_date_total=''
editData_title_total=''
editData_price_total=''

searchwords = raw_input("검색어를 입력하세요: ")
print "----->"+searchwords+"검색 중"

targeturl_first="https://search.shopping.naver.com/search/all.nhn?origQuery="+searchwords+"&pagingIndex=1&pagingSize=80&viewType=list&sort=review&exagency=true&frm=NVSCPRO&query="+searchwords
soup_first = BeautifulSoup(urllib.urlopen(targeturl_first).read(), "html.parser")
editData_first = soup_first.find_all('a', {'class': "_productSet_total"})
editDataStr_first = str(editData_first)

sliced = editDataStr_first.find('</em>') #뒤에서부터 공백이 있는 문자열의 인덱스를 찾아 변수에 저장한다.
editDataStr_first = editDataStr_first[sliced:] #찾아낸 문자열 인덱스 뒤로 다 잘라낸다.
editDataStr_first = editDataStr_first.replace('</em>','')
editDataStr_first = editDataStr_first.replace('</a>]','')


print "----->"+editDataStr_first+"개 데이터"
editDataStr_first = editDataStr_first.replace(',','')
editDataStr_first_Num = int(editDataStr_first)
endPageIndex = int(editDataStr_first, base=10)//80+1
print "----->"+str(endPageIndex)+"개 페이지 검색 시작"

barIndex = endPageIndex+1+editDataStr_first_Num
bar = Bar('Processing', max=barIndex)

for indexNum in range(1, endPageIndex+1):
	targeturl="https://search.shopping.naver.com/search/all.nhn?origQuery="+searchwords+"&pagingIndex="+str(indexNum)+"&pagingSize=80&viewType=list&sort=review&exagency=true&frm=NVSCPRO&query="+searchwords
	contents = requests.get(targeturl).text
	soup = BeautifulSoup(contents, "html.parser")

	for tag in soup.select('span[class=date]'):
		editData_date = tag.text.strip()
		dateList.append(editData_date)
	for tag in soup.select('a[class=tit]'):
		editData_title = tag.text.strip()
		titleList.append(editData_title)
	for tag in soup.select('span[class=price]'):
		editData_price = tag.text.strip()
		priceList.append(editData_price)
	for tag in soup.select('div[class=info]'):
		linkUrl = tag.find('a')['href']
		titleUrlList.append(linkUrl)
	bar.next()

#print "Soup: "+str(editDataStr_first_Num) +", title: "+ str(len(titleList))+", price: "+ str(len(priceList))+", date: "+ str(len(dateList))+", url: "+ str(len(titleUrlList))

for parsingNum in range(0, editDataStr_first_Num):
	dataSet=titleList[parsingNum]+","+priceList[parsingNum]+","+dateList[parsingNum]+","+titleUrlList[parsingNum]
	dataSetList=dataSetList+'\n'+dataSet
	bar.next()

dataUtf = dataSetList.encode('utf-8')
bar.finish()

# writedata.py
f = open("/Users/bomha/Desktop/naver_"+searchwords+".txt", 'w')
f.write(dataUtf)
f.close()