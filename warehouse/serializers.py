from rest_framework import serializers
from .models import Mahsulot, Xomashyo, MahsulotXomashyo, Omborxona


class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ['id', 'nom', 'kod']


class XomashyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xomashyo
        fields = ['id', 'nom']


class MahsulotXomashyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahsulotXomashyo
        fields = ['mahsulot', 'xomashyo', 'miqdori']


class OmborxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omborxona
        fields = ['id', 'xomashyo', 'qolgan_miqdori', 'narx']
