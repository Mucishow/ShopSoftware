"""ShopSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views as pdview
from shopcart import views as listview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', pdview.all),
    path('products/shopList/', pdview.valid_elements),
    path('products/crawl/', pdview.crawl),
    path('products/<id>/', pdview.detail),
    path('list/', listview.show_list),
    path('list/clear/', listview.clear_list),
    path('list/new/', listview.new),
    path('list/addToList/', listview.add),
    path('img/<name>/', pdview.image),
]
