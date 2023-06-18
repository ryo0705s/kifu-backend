# Generated by Django 4.2.1 on 2023-06-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('total_donation_amounts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kifu_app.user')),
            ],
        ),
    ]
