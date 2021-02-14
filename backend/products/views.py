from django.shortcuts import render
from products.models import Product
from utils.response_utils import json_response
from django.http import JsonResponse
import products.crawler as pd_crawler
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def all(request):
    return json_response(Product.objects.values())

def valid_elements(request):
    return json_response(Product.objects.filter(valid=True).values())

def image(request,name):
    with open("img/"+name, "rb") as image_file:
        return HttpResponse(image_file.read(), content_type="image/jpeg")

@csrf_exempt
def crawl(request):
    json_data = json.loads(request.body)
    for item in json_data['itens']:
        pd_crawler.crawl(item);
    return HttpResponse("OK")

def validate(request,id):
    product = Product.objects.get(id=id)
    print(product.valid)

    product.valid = True
    print(product)
    product.save()
    print(product.valid)

    return HttpResponse("OK")
