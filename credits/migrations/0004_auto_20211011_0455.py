# Generated by Django 2.2.24 on 2021-10-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0003_auto_20211011_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitude',
            name='amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='punctuation',
            field=models.CharField(choices=[(2, 'Good'), (1, 'Average'), (0, 'Bad')], default=2, max_length=2),
        ),
        migrations.AlterField(
            model_name='solicitude',
            name='state',
            field=models.CharField(choices=[(0, 'Approved'), (1, 'Disapproved'), (2, 'Pending')], default=0, max_length=2),
        ),
    ]