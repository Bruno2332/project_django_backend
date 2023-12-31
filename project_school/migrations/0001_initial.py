# Generated by Django 4.2.6 on 2023-10-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id_discipline', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id_office', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('rg', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('discipline', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project_school.discipline')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id_team', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rg', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('registration', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfessorTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_professor', models.ManyToManyField(to='project_school.professor')),
                ('id_team', models.ManyToManyField(to='project_school.team')),
            ],
        ),
        migrations.CreateModel(
            name='NoteDiscipline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note_1', models.FloatField()),
                ('note_2', models.FloatField()),
                ('note_3', models.FloatField()),
                ('mean', models.FloatField(blank=True, null=True)),
                ('id_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.discipline')),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.student')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('rg', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.office')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.student')),
            ],
        ),
        migrations.CreateModel(
            name='AddressProfessor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('id_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.professor')),
            ],
        ),
        migrations.CreateModel(
            name='AddressEmployee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_school.employee')),
            ],
        ),
    ]
