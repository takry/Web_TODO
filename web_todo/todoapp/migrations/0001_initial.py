# Generated by Django 3.2.8 on 2022-09-15 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0002_project'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datatime', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
