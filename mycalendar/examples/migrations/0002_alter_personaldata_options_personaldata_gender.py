# Generated by Django 4.1.5 on 2023-01-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldata',
            options={'verbose_name': 'Osoba', 'verbose_name_plural': 'Osoby'},
        ),
        migrations.AddField(
            model_name='personaldata',
            name='gender',
            field=models.CharField(choices=[('f', 'Kobieta'), ('m', 'Mężczyzna'), ('o', 'Nie podaję')], default='n', max_length=1),
            preserve_default=False,
        ),
    ]