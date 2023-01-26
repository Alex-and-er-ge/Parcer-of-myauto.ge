import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate()
# yt = YandexFreeTranslate(api = "web")
# yt = YandexFreeTranslate(api = "ios")
#import lxml
#import re

count=0
UserAgent().chrome

base_url = 'https://api2.myauto.ge/en/products?TypeID=2&ForRent=&Mans=&PriceFrom=600&PriceTo=3000&CurrencyID=1&MileageType=1&Customs=1&Page={}'
for x in range (1,9):
    url = base_url.format(x)
    #print (url)
    request=requests.get(url, headers={'User-Agent': UserAgent().chrome})
    text=request.content
    soup = BeautifulSoup(text, 'html.parser') 
   # for key, value in request.request.headers.items():
        #print(key+": "+value)
    data=json.loads(str(soup))
    for i in data["data"]["items"]:
        if i['engine_volume']>=500 or i['engine_volume']==0:
            print(" ")
            count+=1
            print ('     -======= - ',count,' - =======-    ')
            print(i['order_date'],"  +",i['client_phone'],"  ",i['prod_year'],'year   ',i['engine_volume'],'ccm   ',int(i['price_usd']),'$   ',i['car_model'],)
            pic='https://static.my.ge/myauto/photos/{}/thumbs/{}_1.jpg'          
            pic1=pic.format(i['photo'],i['car_id'])           
            print(pic1)           
            print(" ")          
            try:
                print(yt.translate("ka", "ru", i['car_desc']))             
            except:
                pass
            print(" ")
            
print ("finish!")


#mops='https://www.myauto.ge/en/s/motorcycles?vehicleType=2&bargainType=&mansNModels=&priceFrom=600&priceTo=3000&currId=1&mileageType=1&customs=1&sort=1&page=4'
#request1=requests.get(mops, headers={'User-Agent': UserAgent().chrome})
#text1=request.content
#soup1 = BeautifulSoup(text1, 'html.parser')
#pagination = soup.find_all('a', attrs={'rel'})
#print (pagination)





#<a target="_blank" rel="noopener noreferrer" href="/en/pr/84808903/for-sell-motorcycles-motorcycle-suzuki-gs-500-1993-petrol-tbilisi?offerType=basic">
#<div class="list-item__thumbnail flex-shrink-0 w-m-200px mb-12px mb-m-0 px-16px px-m-0"><div class="list-item__thumbnail__container">
#<div class="list-item__thumbnail__items ratio-4-3 w-100"><div class="items"><div class="items__page"><div class="items__image-wrapper">
#<img class="items__image" src="https://static.my.ge/myauto/photos/0/9/8/0/8/thumbs/84808903_1.jpg?v=0" alt=""></div><div class="items__button">
#</div></div><div class="items__page"><div class="items__image-wrapper"><img class="items__image" src="https://static.my.ge/myauto/photos/0/9/8/0/8/thumbs/84808903_2.jpg?v=0" alt="">
#</div><div class="items__button"></div></div><div class="items__page"><div class="items__image-wrapper">
#<img class="items__image" src="https://static.my.ge/myauto/photos/0/9/8/0/8/thumbs/84808903_3.jpg?v=0" alt=""></div><div class="items__button"></div></div></div></div></div></div></a>



#2023-01-24 04:41:05 1993 995555311138      500     1400     84808903 0/9/8/0/8
#<img class="items__image" src="https://static.my.ge/myauto/photos/0/9/8/0/8/thumbs/84808903_1.jpg?v=0" alt="">

#print(request)
#print(type(data))
#with open("output11.html", "w", encoding="utf-8") as file:
#    file.write(str(soup))

#cont=soup.select('d-flex align-items-center')
#<div class="d-flex align-items-center
#print(cont)

#internalLinks = [ 
    #a.get('h1') for a in soup.find_all("2") 
    #if a.get('h1') and a.get('h1').startswith('/')]

#print(internalLinks) 

#<div class="d-flex align-items-center"><h2 class="d-flex font-medium text-gray-800 font-size-14"><a class="text-gray-800" target="_blank" rel="noopener noreferrer" href="/en/pr/81742231/for-sell-motorcycles-moped-tvs-2021-petrol-tbilisi?offerType=basic">TVS ntorq race edition</a><span class="ml-8px d-flex text-gray-500 font-medium text-nowrap">2021 y</span></h2></div>



