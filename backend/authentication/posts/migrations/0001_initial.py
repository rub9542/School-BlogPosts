# Generated by Django 3.0.3 on 2020-03-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title', max_length=100)),
                ('post', models.TextField(help_text='Enter the posts', max_length=500)),
            ],
        ),
    ]
