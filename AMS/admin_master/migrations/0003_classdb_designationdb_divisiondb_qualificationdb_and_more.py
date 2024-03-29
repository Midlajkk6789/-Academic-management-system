# Generated by Django 5.0.1 on 2024-01-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0002_employeecatagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'deactive')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Designationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designationName', models.CharField(max_length=255)),
                ('designationCode', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'deactive')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Divisiondb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisionName', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'deactive')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Qualificationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'active'), (0, 'deactive')], default=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='Department',
            new_name='Departmentdb',
        ),
        migrations.RenameModel(
            old_name='EmployeeCatagory',
            new_name='EmployeeCatagorydb',
        ),
    ]
