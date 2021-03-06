# Generated by Django 3.1 on 2020-09-08 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateField(auto_now_add=True, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.poll'),
            preserve_default=False,
        ),
    ]
