from django.db import models

# Create your models here.

class GuestBook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='작성자', max_length=50)
    message = models.TextField(verbose_name='메시지')
    created_at = models.DateTimeField(verbose_name='작성 일시', auto_now_add=True)