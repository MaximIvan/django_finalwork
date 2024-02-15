# Generated by Django 5.0.2 on 2024-02-15 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='категория')),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(default='rootRecipe', max_length=200)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок*')),
                ('description', models.TextField(verbose_name='Описание*')),
                ('steps_cook', models.TextField(blank=True, verbose_name='Шаги')),
                ('time_cook', models.IntegerField(verbose_name='Готовка в мин*')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='фото')),
                ('ingredients', models.TextField(verbose_name='Ингредиенты*')),
                ('views', models.IntegerField(default=0, verbose_name='Кол просмотров')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('change_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('calories', models.IntegerField(blank=True, verbose_name='Ккал*')),
                ('estimation_average', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Средний бал')),
                ('author', models.CharField(max_length=200, verbose_name='имя автора*')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recipesapp.category', verbose_name='Категории*')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['-change_at', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('estimation', models.DecimalField(decimal_places=1, max_digits=2)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('change_at', models.DateField(auto_now_add=True)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipesapp.recipe')),
            ],
        ),
    ]