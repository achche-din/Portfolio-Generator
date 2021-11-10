from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='info')
    registration_number=models.IntegerField()
    college_email_id=models.EmailField()
    other_emails=models.TextField() 
    branch=models.CharField(max_length=50)
    year=models.IntegerField()
    def __str__(self):
        return self.user.username

class Hero(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='hero')
    title=models.CharField(max_length=50)
    tags=models.TextField()
    def __str__(self):
        return self.title

class About(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='about')
    description=models.TextField()
    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='education')
    type=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    start_year=models.DateField()
    end_year=models.DateField()
    description=models.TextField()
    def __str__(self):
        return self.title

class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='experience')
    position=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    start_year=models.DateField()
    end_year=models.DateField()
    description=models.TextField()
    def __str__(self):
        return self.title

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
    title=models.CharField(max_length=50)
    description=models.TextField()
    link=models.URLField(blank=True)
    tags=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    def __str__(self):
        return self.title

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='skills')
    title=models.TextField()
    

class Achievement(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='achievements')
    title=models.TextField()
    link=models.TextField(blank=True)
    description=models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="blogs")
    tags =models.TextField()
    content=models.TextField()
    up_Votes=models.IntegerField(default=0)
    down_Votes=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    is_active= models.BooleanField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=CASCADE)
    up_Votes=models.IntegerField(default=0)
    down_Votes=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username