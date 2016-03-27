from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=100)  # Возможно сделать не обязательным
    date_create = models.DateTimeField()  # Поле для даты и времени создания записи
    text = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title
