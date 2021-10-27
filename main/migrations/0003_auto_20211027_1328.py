# Generated by Django 3.2.7 on 2021-10-27 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reply_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='reply',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.rating'),
        ),
    ]
