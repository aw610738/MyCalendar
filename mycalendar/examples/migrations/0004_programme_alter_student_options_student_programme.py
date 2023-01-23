# Generated by Django 4.1.5 on 2023-01-14 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Kierunek studiów',
                'verbose_name_plural': 'Kierunki studiów',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Studenci'},
        ),
        migrations.AddField(
            model_name='student',
            name='programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='examples.programme'),
        ),
    ]
