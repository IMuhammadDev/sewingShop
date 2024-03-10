from django.contrib import admin
from .models import Mahsulot, Xomashyo, MahsulotXomashyo, Omborxona


@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['nom', 'kod']


@admin.register(Xomashyo)
class XomashyoAdmin(admin.ModelAdmin):
    list_display = ['nom']


@admin.register(MahsulotXomashyo)
class MahsulotXomashyoAdmin(admin.ModelAdmin):
    list_display = ['mahsulot', 'xomashyo', 'miqdori']


@admin.register(Omborxona)
class OmborxonaAdmin(admin.ModelAdmin):
    list_display = ['xomashyo', 'qolgan_miqdori', 'narx']
