from django.db import models

class City(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name='Город')
    cian_id = models.IntegerField(db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class District(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name='Район')
    cian_id = models.IntegerField(db_index=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Номер города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class Metro(models.Model):
    name = models.CharField(max_length=50, verbose_name='Метро')
    cian_id = models.IntegerField(db_index=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Номер города')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'cian_id')
        verbose_name = 'Метро'
        verbose_name_plural = 'Метро'

class Rooms(models.Model):
    roomnum = models.IntegerField()

    def __str__(self):
        return str(self.roomnum)

    class Meta:
        verbose_name = 'Количество комнат'
    