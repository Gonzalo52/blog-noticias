from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('posts/', views.posts),
    path('post/<int:id>', views.post),
    path('classifieds/', views.classifieds),
    path('classified/<int:id>', views.classified),
]