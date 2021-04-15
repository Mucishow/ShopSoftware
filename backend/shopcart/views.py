from django.shortcuts import render
from shopcart.models import ShopItem, ShopList
from utils.response_utils import json_response
from django.http import JsonResponse
from django.http import HttpResponse
import json
from products.models import Product
from decimal import *

# Create your views here.
def show_list(request):
    list = [];
    total_price = Decimal(0);
    for shopItem in ShopItem.objects.filter(list_name_id=1):
        list.append({"PRODUTO":shopItem.item.name,"QUANTIDADE": shopItem.quantity,"PREÇO UNIDADE":round(shopItem.item.price,2),"PREÇO":round(shopItem.item.price*shopItem.quantity,2)})
        total_price = total_price + shopItem.item.price*shopItem.quantity
    print(list)
    print(round(total_price,2))
    return JsonResponse({"Lista":list, "PREÇO": round(total_price,2)})

def add(request):
    json_data = json.loads(request.body)
    product = Product.objects.get(id=json_data['item']["id"])
    quantity = json_data['quantity']
    shopList = ShopList.objects.get(id=1)
    
    ShopItem.objects.filter(list_name=shopList,item=product).delete()

    if(int(quantity) > 0):
        shopItem = ShopItem(item = product,quantity=quantity,list_name=shopList)
        shopItem.save()

    return json_response(shopList.items.all().values())

def new(request):
    shopList = ShopList()
    shopList.save();
    return HttpResponse("CREATED");

def clear_list(request):
    ShopList.objects.get(id=1).items.all().delete()
    return HttpResponse("LIST CLEARED");
