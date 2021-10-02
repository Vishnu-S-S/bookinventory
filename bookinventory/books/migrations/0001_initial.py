# Generated by Django 2.2.24 on 2021-10-02 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=256)),
                ('book_author', models.CharField(blank=True, max_length=64, null=True)),
                ('book_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_books', to='books.Books')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='books.Books')),
                ('borrowed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]