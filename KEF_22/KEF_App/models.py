from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=100, null=True)
    school_region = models.CharField(max_length=100, null=True)
    school_password = models.CharField(max_length=100)
    school_email = models.EmailField(max_length=100, null=True, unique=True)
    school_teachers_count = models.CharField(max_length=100, null=True)
    school_classroom_count = models.CharField(max_length=100, null=True)



class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100, null=True)
    teacher_email = models.EmailField(max_length=100, unique=True, null=True)
    teacher_password = models.CharField(max_length=100, null=True)
    

class Student(models.Model):
    student_name = models.CharField(max_length=100, null=True)
    student_school = models.CharField(max_length=100, null=True)
    student_score = models.CharField(max_length=100, null=True)
    student_grade = models.CharField(max_length=100, null=True)


class Assesment(models.Model):
    assesment_name = models.CharField(max_length=100, null=True)
    assesment_subject = models.CharField(max_length=100, null=True)
    assesment_date = models.DateField()


class Training(models.Model):
    training_name = models.CharField(max_length=100, null=True)
    training_subject = models.CharField(max_length=100, null=True)
    training_date = models.DateField()
    training_hours = models.CharField(max_length=100, null=True)


class Assesment_Teacher(models.Model):
    test_id = models.ForeignKey(Assesment, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    test_score = models.CharField(max_length=100, null=True)

class Training_Teacher(models.Model):
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class School_Teacher(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
