# Generated by Django 3.2.5 on 2021-10-13 21:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('platform', models.CharField(choices=[('macOS', 'macOS'), ('Windows', 'Windows')], max_length=7)),
                ('subscription', models.CharField(blank=True, choices=[('Premium', 'Premium'), ('Basic', 'Basic')], max_length=8, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Incompleted', 'Incompleted')], max_length=11, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=models.SET('Unknown'), to='dashboard.customer')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=11, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Answered', 'Answered'), ('Missed', 'Missed')], max_length=8, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=models.SET('Unknown'), to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=models.SET('Unknown'), to='dashboard.customer')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
