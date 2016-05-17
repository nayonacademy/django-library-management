from django.db import models

# Create your models here.


class AddStudent(models.Model):
    name = models.CharField(max_length=45)
    father_name = models.CharField(max_length=45)
    mother_name = models.CharField(max_length=45)
    unique_id = models.CharField(max_length=45, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=45)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class AddBook(models.Model):
    book_name = models.CharField(max_length=45)
    author_name = models.CharField(max_length=45)
    unique_no = models.CharField(max_length=45, null=True, blank=True, unique=True)
    category_name = models.ForeignKey(Category)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.book_name

# BookDistribution
class LogFile(models.Model):
    student_id = models.ForeignKey(AddStudent)
    book_id = models.ForeignKey(AddBook)
    return_status = models.BooleanField(default=0)
    amount = models.IntegerField()

    def __str__(self):
        return self.borrow


class Revenue(models.Model):
    amount = models.IntegerField()
    student_id = models.ForeignKey(AddStudent)

    def __str__(self):
        return self.amount
