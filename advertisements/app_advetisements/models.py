from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisements(models.Model):
    tittle = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('торг', help_text = 'Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add = True)
    updeted_at = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id = {self.id}, title = {self.tittle}, price = {self.price}"
    
    @admin.display(description = 'Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: green; font-weight: bold;"> Сегодня В {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description = 'Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updeted_at.date() == timezone.now().date():
            updated_time = self.updeted_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: red; font-weight: bold;"> Сегодня В {} </span>', updated_time
            )
        return self.updeted_at.strftime('%d.%m.%Y в %H:%M:%S')

# Create your models here.
