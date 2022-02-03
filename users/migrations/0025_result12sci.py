# Generated by Django 3.2.8 on 2022-01-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_result12comm'),
    ]

    operations = [
        migrations.CreateModel(
            name='result12sci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(blank=True, max_length=254)),
                ('question', models.CharField(default='', max_length=1000)),
                ('answer', models.CharField(choices=[('Dislike', 'Dislike'), ('Neutral', 'Neutral'), ('Enjoy', 'Enjoy')], max_length=9)),
            ],
        ),
    ]
