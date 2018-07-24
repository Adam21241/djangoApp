from django.db import models
from datetime import date



class Sala(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=1000)



    def __str__(self):
        return self.nazwa

class Wydarzenie(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    podajdate = models.DateField(default=date(2016, 1, 1))
    s_hour = models.IntegerField(default=10)
    e_hour = models.IntegerField(default=11)
    kto = models.CharField(max_length=20, default='')


    def __str__(self):
        return 'Użytkownik ' + self.kto + ' zarezerwował: ' + self.sala.nazwa + ' w dniu ' + str(self.podajdate) + ' od godziny ' + str(self.s_hour) + ':00 do godziny ' + str(self.e_hour) + ':00'