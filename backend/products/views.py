from django.shortcuts import render
from products.models import Product
from utils.response_utils import json_response
from django.http import JsonResponse
import products.crawler as pd_crawler
from django.http import HttpResponse
import json
import os

# Create your views here.
def all(request):
    return json_response(Product.objects.filter(valid=False).values())

def valid_elements(request):
    return json_response(Product.objects.filter(valid=True).values())

def image(request,name):
    with open("img/"+name, "rb") as image_file:
        return HttpResponse(image_file.read(), content_type="image/jpeg")

def crawl(request):
    json_data = json.loads(request.body)
    for item in json_data['itens']:
        pd_crawler.crawl(item);
    return HttpResponse("OK")

def detail(request,id):
    if(request.method == "POST"):
        product = Product.objects.get(id=id)

        product.valid = True
        product.save()

        return HttpResponse("OK")
    elif(request.method == "DELETE"):
        product = Product.objects.get(id=id)
        os.remove("img/"+str(product.picture))
        Product.objects.filter(id=id).delete()
        return HttpResponse("DELETED")


