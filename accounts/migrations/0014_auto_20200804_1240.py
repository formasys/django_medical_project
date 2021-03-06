# Generated by Django 3.0.8 on 2020-08-04 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200804_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='rendezvous',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Rendezvous'),
        ),
        migrations.AddField(
            model_name='ordonnance',
            name='rendezvous',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Rendezvous'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='rv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Patient'),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='rv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Patient'),
        ),
    ]
