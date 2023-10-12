from django.db import models

class Discipline(models.Model):
    id_discipline = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Office(models.Model):
    id_office = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Person(models.Model):
    rg = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        abstract = True


class Student(Person):
    registration = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)


class Professor(Person):
    discipline = models.OneToOneField('Discipline', on_delete=models.CASCADE)
    salary = models.FloatField()
    

class Employee(Person):
    office = models.ForeignKey('Office', on_delete=models.CASCADE)
    salary = models.FloatField()


class AddressStudent(models.Model):
    id = models.AutoField(primary_key=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


class AddressProfessor(models.Model):
    id = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


class AddressEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    id_employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


class ProfessorTeam(models.Model):
    id = models.AutoField(primary_key=True)
    id_professor = models.ManyToManyField('Professor')
    id_team = models.ManyToManyField('Team')


class NoteDiscipline(models.Model):
    id = models.AutoField(primary_key=True)
    id_discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    note_1 = models.FloatField()
    note_2 = models.FloatField()
    note_3 = models.FloatField()
    mean = models.FloatField(null=True, blank=True)
    
    def calcular_media(self):
        return (self.nota_1 + self.nota_2 + self.nota_3) / 3

    def save(self, *args, **kwargs):
        self.mean = self.calcular_media()
        super(Student, self).save(*args, **kwargs)