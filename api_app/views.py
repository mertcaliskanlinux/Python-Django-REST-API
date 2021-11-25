from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import CardItemSerializers
from .models import CardItem


class CardItemViews(APIView):
    #POST İstek gövdesinde bulunan sunucuya veri göndermek için bir istek'te bulunur.
    def post(self,request):
        serializer = CardItemSerializers(data=request.data)
        
        if serializer.is_valid():
            #kaydet
            serializer.save()
            return Response ({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response ({"status":"success","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,id=None):

        if id:
            item = CardItem.objects.get(id=id)
            serializer = CardItemSerializers(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)


        items = CardItem.objects.all()
        serializer = CardItemSerializers(items,many=True)
        return Response ({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

    
    def patch(self,request,id=None):
        # CARDITEM GÜNCELLEMEK İSTEDİĞİMİZ MODEL
        item = CardItem.objects.get(id=id)
        #İSTEK ALINAN VERİLER VE PARTİAL=TRUE MODELİMİZİN TÜM ALANLARINI İÇERMEYEBİLECEĞİNİ BELİRTMEK İÇİN.
        serializer = CardItemSerializers(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

        else:
            return Response({"status":"error","data":serializer.errors})


    def delete(self,request,id=None):
        #NESNEYİ GETİR
        item = get_object_or_404(CardItem,id=id)
        #NESNEYİ SİL
        item.delete()
        #GERİ CEVAP DÖN
        return Response({"status":"success","data":"Item Deleted"})
