from django.db import models


#MODEL SINIFI
class CardItem(models.Model):
    #ÜRÜN İSMİ
    product_name = models.CharField(max_length=254)
    #ÜRÜN FİYATI
    product_price = models.FloatField()
    #ÜRÜN MİKTARI (STOK)
    product_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name
