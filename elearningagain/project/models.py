

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class author(models.Model):
    profile_pic=models.FileField()
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    details=models.TextField()

    def __str__(self):
        return self.name.username

class category(models.Model):
    name=models.CharField(max_length=200)


    def __str__(self):
        return self.name

class subcategory(models.Model):
    name=models.CharField(max_length=200)
    details = models.TextField()
    image = models.FileField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    syllebus=models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name

class article(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    body=models.TextField()
    title=models.CharField(max_length=200)
    posted_on=models.DateField(auto_now=False,auto_now_add=True)
    updated_on=models.DateField(auto_now=True,auto_now_add=False)
    image=models.FileField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class events(models.Model):
    events_author=models.ForeignKey(author,on_delete=models.CASCADE)
    body=models.TextField()
    name=models.CharField(max_length=200)
    posted_on = models.DateField(auto_now=False, auto_now_add=True)
    updated_on = models.DateField(auto_now=True, auto_now_add=False)
    start_date=models.DateField()
    finish_date=models.DateField()
    image=models.FileField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    venue=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class comment(models.Model):
    post=models.ForeignKey(article,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    post_comment=models.TextField()

    def __str__(self):
        return self.post.title
class videolectures(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=255, blank=True)
    video_file = models.FileField(upload_to='documents/')
    document=models.FileField(upload_to='documents/')
    video_author=models.ForeignKey(author,models.CASCADE)
    subcategory=models.ForeignKey(subcategory,models.CASCADE)
    category=models.ForeignKey(category,models.CASCADE)
    posted_on = models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.title
class videocomment(models.Model):
    post=models.ForeignKey(videolectures,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    post_comment=models.TextField()

    def __str__(self):
        return self.post.title
class coursefaq(models.Model):
    coursename=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()

    def __str__(self):
        return self.question
class forumcomment(models.Model):
    post=models.ForeignKey(subcategory,null=True,blank=True,on_delete=models.CASCADE)
    content=models.TextField()
    reply=models.ForeignKey('forumcomment',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)