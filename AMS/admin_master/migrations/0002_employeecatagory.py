# Generated by Django 5.0.1 on 2024-01-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeCatagory', models.CharField(max_length=255)),
                ('employeeArea', models.IntegerField(choices=[(1, 'Accountant'), (2, 'Teacher'), (3, 'Library'), (4, 'Cafteria'), (5, 'Other')])),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'deactive')], default=1)),
            ],
        ),
    ]
