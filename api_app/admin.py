from django.contrib import admin

#MODELİMİZİ İMPORT ETMELİYİZ
from api_app.models import CardItem


#MODELİMİZİ ADMİN PANELDE ERİŞEBİLMEMİZ İÇİN
admin.site.register(CardItem)