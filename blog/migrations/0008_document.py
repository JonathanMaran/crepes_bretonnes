# Generated by Django 2.2.5 on 2020-06-12 11:52

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('doc', models.FileField(upload_to=blog.models.renommage, verbose_name='Document')),
            ],
        ),
    ]
