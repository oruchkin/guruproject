from django.db import models


class Time_Stamped_Mixin(models.Model):
    """ Абстрактный класс для присваивания к моделям двух полей с датами """
    created = models.DateTimeField('обьект создан', auto_now_add=True)
    modified = models.DateTimeField('обьект изменен', auto_now=True)
    class Meta:
        abstract = True


class Shop(Time_Stamped_Mixin):
    title = models.CharField(max_length = 150)
    city = models.ForeignKey("guruapp.City", verbose_name='Город', on_delete=models.CASCADE)
    street = models.ForeignKey("guruapp.Street", verbose_name='Улица', on_delete=models.CASCADE)
    house = models.CharField(max_length = 150)
    time_open = models.TimeField(auto_now=False, auto_now_add=False)
    time_closed = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title


class City(Time_Stamped_Mixin):
    title = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.title


class Street(Time_Stamped_Mixin):
    city = models.ForeignKey("guruapp.City", verbose_name='город', on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    
    
    def __str__(self):
        return self.title