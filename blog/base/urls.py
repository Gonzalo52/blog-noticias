from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post/<int:id>', views.post),
    path('opinions/', views.opinions),
    #clasificados
    path('created/', views.created_classified),
    path('created/<int:id>', views.created_classified),
    path('comment/', views.comment),
    #registro, inicio, cierre de sesion
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logoutPage),
    #autores
    path('author1/', views.author1),
    path('author2/', views.author2),
    path('author3/', views.author3),
    path('author4/', views.author4),
    path('author5/', views.author5),
    #clasificacion de noticias
    path('present/', views.present),
    path('police/', views.police),
    path('sports/', views.sports),
    path('technology/', views.technology),
    path('economy/', views.economy),
    path('classified/', views.classified),
]