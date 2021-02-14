from bs4 import BeautifulSoup
import requests
from PIL import Image
import urllib.request as urllib2
from datetime import datetime
from products.models import Product
import io
from re import sub
from decimal import Decimal
import uuid

def clean_price(price):
    return price[2:10].replace(" ","").replace("\r","").replace("\n","")

def save_image(im):
    name = str(uuid.uuid4())+".jpg"
    im.save("img/"+name)
    return name
    
def crawl(item):
    url_continente = 'https://www.continente.pt/pt-pt/public/Pages/searchresults.aspx?k='

    response = requests.get(url_continente+item)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    continente_products = html_soup.find_all("div",{'class':'productBoxTop'})
    for product in continente_products:
        name_and_size = product.find("div",{'class': "containerDescription"});
        name = name_and_size.find("a").text
        size = name_and_size.find("div",{'class': "subTitle"}).text.lower()
        price = clean_price(product.find("div",{'class':"priceFirstRow"}).text)
        image = product.find("div",{'class':"image"})
        im = Image.open(urllib2.urlopen(image.find("img")['data-original']),mode='r')
        save_image(im)
        product = Product(name=name,picture=save_image(im),size=size,price=Decimal(price.replace(",",".")),update_time=datetime.now(),valid=False)
        product.save()
