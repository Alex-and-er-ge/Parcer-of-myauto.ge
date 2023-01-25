import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

#import lxml
#import re


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
            print(i['order_date'],i['prod_year'],i['client_phone'],i['car_model'],'   ',i['engine_volume'],'   ',i['price_usd'],'   ',i['car_id'])


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



