# Generated by Django 2.2.5 on 2020-06-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
