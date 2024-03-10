from rest_framework import generics
from .models import Mahsulot, Xomashyo, Omborxona
from .serializers import MahsulotSerializer, XomashyoSerializer, OmborxonaSerializer


class MahsulotlarList(generics.ListCreateAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer


class MahsulotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer


class XomashyolarList(generics.ListCreateAPIView):
    queryset = Xomashyo.objects.all()
    serializer_class = XomashyoSerializer


class XomashyoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Xomashyo.objects.all()
    serializer_class = XomashyoSerializer


class OmborxonalarList(generics.ListCreateAPIView):
    queryset = Omborxona.objects.all()
    serializer_class = OmborxonaSerializer


class OmborxonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Omborxona.objects.all()
    serializer_class = OmborxonaSerializer
