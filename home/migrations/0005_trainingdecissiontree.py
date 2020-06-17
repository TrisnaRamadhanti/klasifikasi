# Generated by Django 3.0.4 on 2020-06-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_trainingsvmsmo_epsilon'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDecissionTree',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('k_fold', models.CharField(blank=True, max_length=100, null=True, verbose_name='KFold (Split)')),
            ],
        ),
    ]
