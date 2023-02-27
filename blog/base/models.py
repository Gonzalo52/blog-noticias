from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoty(models.Model):
    classification = models.CharField(max_length = 200, null = False, blank = False)
    

    def __str__(self):
        return self.classification


class Author(models.Model):
    name = models.CharField(max_length = 200, null = False, blank = False)
    last_name = models.CharField(max_length = 200, null = False, blank = False)
    comment = models.TextField()
    category = models.ForeignKey(Categoty, on_delete = models.SET_NULL, null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True)
    category = models.ForeignKey(Categoty, on_delete = models.SET_NULL, null = True, blank = False)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


#opiniones sobre post
class Opinions(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Classified(models.Model):
    title = models.CharField(max_length = 150, null = False, blank = False)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


#comentarios sobre clasificados
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    classified = models.ForeignKey(Classified, null = True, on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text