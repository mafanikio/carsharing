from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    age = models.IntegerField(default=0, verbose_name="Возраст")
    exp = models.IntegerField(default=0, verbose_name="Стаж")
    text = models.CharField(max_length=300, verbose_name="Комментарий")
    type = models.CharField(max_length=300, verbose_name="Тип ТС")
    rating = models.IntegerField(default=5, verbose_name="Рейтинг")
    status = models.BooleanField(default=False, verbose_name="Статус")
    photo = models.ImageField(default='', upload_to="mysite/photos/", verbose_name="Фото")
    license = models.ImageField(default='', upload_to="mysite/licenses/", verbose_name="Права")
    phone = models.CharField(max_length=300, verbose_name="Телефон")

    def __str__(self):
        return self.name + ' ' + self.surname


class Car(models.Model):
    maker = models.CharField(max_length=300, default='', verbose_name="Марка")
    model = models.CharField(max_length=300, verbose_name="Модель")
    year = models.IntegerField(default=0, verbose_name="Год выпуска")
    type = models.CharField(max_length=300, verbose_name="Тип")
    text = models.CharField(max_length=300, verbose_name="Описание")
    last_service = models.DateTimeField(verbose_name="Последнее ТО", blank=True, null=True)
    rented = models.BooleanField(default=False, verbose_name="Сдается")
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Прикрепленный водитель", blank=True,
                              null=True)
    picture = models.ImageField(default='', upload_to="mysite/cars/", verbose_name="Фото")

    def __str__(self):
        return self.maker


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Авто")
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Водитель", blank=True, null=True)
    date = models.DateTimeField(verbose_name="Дата заказа")
    text = models.CharField(max_length=300, verbose_name="Комментарий")
    complete = models.BooleanField(verbose_name="Статус")

    def __str__(self):
        return self.text


class Services(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наименование работ")
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    date = models.DateTimeField(verbose_name="Время начала работ")
    text = models.CharField(max_length=300, verbose_name="Комментарий")
    complete = models.BooleanField(default=False, verbose_name="Статус")

    def __str__(self):
        return self.vehicle.model


class Detail(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наименование")
    text = models.CharField(max_length=300, verbose_name="Описание")
    price = models.IntegerField(default=0, verbose_name="Цена")
    stock = models.IntegerField(default=True, verbose_name="Штук в наличии")


    def __str__(self):
        return self.name
