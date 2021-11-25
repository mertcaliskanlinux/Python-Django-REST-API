from django.urls import path
from .views import CardItemViews
#İlk argümanı, path() viewslere erişilebilir olacağı alt yoldur ve ikinci argüman, 
# as_view() işlemek için oluşturduğumuz sınıf adıdır 
urlpatterns = [
    #alanadi.com/api/card-items/
    path('card-items/',CardItemViews.as_view()),
    #alanadi.com/api/card-items/İD (ÜRÜN İDSİ)
    #SAYFALAMA
    path('card-items/<int:id>',CardItemViews.as_view())
]
