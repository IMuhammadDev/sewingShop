from django.db import models


class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    kod = models.CharField(max_length=50)


class Xomashyo(models.Model):
    nom = models.CharField(max_length=100)


class MahsulotXomashyo(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    xomashyo = models.ForeignKey(Xomashyo, on_delete=models.CASCADE)
    miqdori = models.FloatField()


class Omborxona(models.Model):
    xomashyo = models.ForeignKey(Xomashyo, on_delete=models.CASCADE)
    qolgan_miqdori = models.FloatField()
    narx = models.FloatField()