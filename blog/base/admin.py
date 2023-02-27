from django.contrib import admin

# Register your models here.

from .models import Categoty, Author, Post, Opinions, Classified, Comment

admin.site.register(Categoty)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Opinions)
admin.site.register(Classified)
admin.site.register(Comment)
