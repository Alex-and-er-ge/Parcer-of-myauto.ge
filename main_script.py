import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate()
# yt = YandexFreeTranslate(api = "web")
# yt = YandexFreeTranslate(api = "ios")
#import lxml
import re

count=0
UserAgent().chrome
file=[]


base_url = 'https://api2.myauto.ge/en/products?TypeID=2&ForRent=&Mans=&PriceFrom=600&PriceTo=3000&CurrencyID=1&MileageType=1&Customs=1&Page={}'
for x in range (1,10):
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
            print(i['order_date'],"  +",i['client_phone'],"  ",i['prod_year'],'year   ',i['engine_volume'],'ccm   ',int(i['price_usd']),'$   ',i['location_id'], i['car_model'],)
            pic='https://static.my.ge/myauto/photos/{}/thumbs/{}_1.jpg'          
            pic1=pic.format(i['photo'],i['car_id'])           
            print(pic1)           
            print(" ")          
            try:
                print(yt.translate("ka", "ru", i['car_desc']))             
            except:
                pass
            print(" ")
            file.append(int(i['price_usd']))
            
print ("finish!")
print(request)
print(file)


f = open("output11.txt", "a")
f.write(str(file))
f.write("\n")
f.close()

