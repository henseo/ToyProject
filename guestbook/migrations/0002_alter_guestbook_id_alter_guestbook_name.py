# Generated by Django 4.2.1 on 2023-05-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='name',
            field=models.CharField(max_length=50, verbose_name='작성자'),
        ),
    ]