# Generated by Django 5.0.3 on 2024-04-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comment_stars_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='cover/'),
        ),
    ]
