from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя организации")

    def __str__(self):
        return self.name


class Adress(models.Model):
    name = models.CharField(max_length=150, verbose_name="Адрес")
    organization = models.ForeignKey('Organization', on_delete=models.PROTECT, null=False, verbose_name="Организация")

    def __str__(self):
        return self.name


class ConsumingOtoplenie(models.Model):
    adress = models.ForeignKey('Adress', on_delete=models.PROTECT, null=False, verbose_name="Адрес")
    fact = models.FloatField(default=0)
    limit = models.FloatField(default=0) # Временно
    # otklonenie = models.FloatField(default=0)
    #month = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")

    def save(self, *args, **kwargs):
        otklonenie = self.limit - self.fact
        super(ConsumingOtoplenie, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.adress)
