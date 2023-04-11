from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    """Фильм"""
    name = models.CharField(max_length=255, verbose_name='Название фильма')
    duration = models.CharField(max_length=50, verbose_name='Длительность')
    rental_start_date = models.DateField(verbose_name='Дата начала проката')
    rental_finish_date = models.DateField(verbose_name='Дата окончания проката')
    sales_company = models.CharField(max_length=255, verbose_name='Кинокомпания')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

class Saloon(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название зала')
    count_place = models.IntegerField(verbose_name='Количество мест')
    description = models.CharField(max_length=50, verbose_name='Описание')
    number_of_rows = models.IntegerField(verbose_name='Номер ряда')
    number_of_places = models.IntegerField(verbose_name='Номер места')

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
        ordering = ['name']

    def __str__(self):
        return str(self.name)

class Seans(models.Model):
    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Зал', related_name='saloon_session')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм', related_name='movie_session')

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
        ordering = ['movie']

    def __str__(self):
        return str(self.saloon)

class JobTitle(models.Model):
    title = models.CharField(max_length=100, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['title']
    
    def __str__(self) -> str:
        return self.title

class Places(models.Model):
    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Зал')
    row_number = models.IntegerField(verbose_name='Номер ряда')
    row_place = models.IntegerField(verbose_name='Номер места')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['saloon']

    def __str__(self) -> str:
        return str(self.saloon)

class SectorSaloon(models.Model):
    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Зал')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=50, verbose_name='Описание')

    class Meta:
        verbose_name = 'Сектор'
        verbose_name_plural = 'Сектора'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

class Employees(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='Имя')
    title = models.ForeignKey(JobTitle, on_delete=models.CASCADE,max_length=40, verbose_name='Должность')
    password = models.CharField(max_length=100, verbose_name='Пароль')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

class PriceForTickets(models.Model):
    seanse = models.ForeignKey(Seans, on_delete=models.CASCADE, verbose_name='Сеансы')
    sector = models.ForeignKey(SectorSaloon, on_delete=models.CASCADE, verbose_name='Сектор')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Цена билета'
        verbose_name_plural = 'Цена билетов'
        ordering = ['seanse']

class Tickets(models.Model):
    ticket_number = models.IntegerField(verbose_name='Номер билета')
    date_created = models.DateField(verbose_name='Дата')
    seanses = models.ForeignKey(Seans, on_delete=models.CASCADE, verbose_name='Сеанс')
    places = models.ForeignKey(Places, on_delete=models.CASCADE, verbose_name='Место')
    played = models.BooleanField(verbose_name='Оплачено')
    booking = models.BooleanField(verbose_name='Бронь')
    creashed = models.BooleanField(verbose_name='creashed')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['seanses']

    def __str__(self) -> str:
        return str(self.ticket_number)
    

class MovingTickets(models.Model):
    moving_tickets = models.IntegerField(verbose_name="Движение билетов")
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, verbose_name='Номер билета')
    date_create = models.DateField(verbose_name='Дата')
    operation = models.CharField(max_length=50, verbose_name='Операция')
    # employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Сотрудник')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Продавец', related_name='seller')

    class Meta:
        verbose_name = 'Движение билета'
        verbose_name_plural = 'Движение билетов'
        ordering = ['ticket']
