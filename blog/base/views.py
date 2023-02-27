from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment, Categoty, Classified, Author, Opinions
from django.contrib import messages
# Create your views here.


#iniciar sesion
def loginPage(request):
    context = {}
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Datos validados")
                return redirect('/')

        messages.error(request, "Datos incorrectos")

    return render(request, 'login.html', context)


#cerrar sesion
def logoutPage(request):
    logout(request)
    return redirect('/')


#regitrar user nuevo
def registerPage(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/register')
        User.objects.create_user(username=username, email=email, first_name=name, last_name=last_name, password=password)
        return redirect('/login')
    return render(request, 'register.html')


#mostrar todos los posts en pagina principal
def home(request):
    posts = Post.objects.order_by("-created")
    return render(request, 'home.html', { 'posts': posts})


#mostrar el post correspondiente
def post(request, id = None):
    post = Post.objects.filter(id = id)
    return render(request, 'post.html', {'post': post})


#opinion sobre post
def opinions(request):
    post = Post.objects.get(id = request.POST.get('post'))
    Opinions.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        post = post
        )
    return redirect('/post')


#funciones para iterar y ver cada autor por separado
def author1(request, id = None):
    author = Author.objects.filter(id = 1)
    posts = Post.objects.filter(author_id = 1)
    return render(request, 'author.html',  {'author': author, 'posts':posts})


def author2(request, id = None):
    author = Author.objects.filter(id = 2)
    posts = Post.objects.filter(author_id = 2)
    return render(request, 'author.html',  {'author': author, 'posts':posts})


def author3(request, id = None):
    author = Author.objects.filter(id = 3)
    posts = Post.objects.filter(author_id = 3)
    return render(request, 'author.html',  {'author': author, 'posts':posts})


def author4(request, id = None):
    author = Author.objects.filter(id = 4)
    posts = Post.objects.filter(author_id = 4)
    return render(request, 'author.html',  {'author': author, 'posts':posts})


def author5(request, id = None):
    author = Author.objects.filter(id = 5)
    posts = Post.objects.filter(author_id = 5)
    return render(request, 'author.html',  {'author': author, 'posts':posts})


#Funciones para ver las direfentes categorias
def present(request):
    posts = Post.objects.filter(category_id = 4)
    return render(request, 'category.html', {'posts': posts})


def economy(request, id = None):
    posts = Post.objects.filter(category_id = 3)
    return render(request, 'category.html', {'posts': posts})


def police(request, id = None):
    posts = Post.objects.filter(category_id = 2)
    return render(request, 'category.html', {'posts': posts})


def technology(request, id = None):
    posts = Post.objects.filter(category_id = 6)
    return render(request, 'category.html', {'posts': posts})


def sports(request, id = None):
    posts = Post.objects.filter(category_id = 5)
    return render(request, 'category.html', {'posts': posts})


def classified(request, id = None):
    classifieds = Classified.objects.order_by('-created')
    return render(request, 'classified.html', {'classifieds': classifieds})


#crear clasificados
def created_classified(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if (id is None):
            Classified.objects.create(
                title = request.POST.get('title'),
                text = request.POST.get('text'),
                user = request.user
            )
            messages.success(request, "Publicaste un nuveo post")
            return redirect("/classified")
        else:
            c = Classified.objects.get(id = id)
            if (c.user == request.user):
                c.title = request.POST.get('title')
                c.text = request.POST.get('text')
                c.save()

    context = {}
    if id is not None:
        c = Classified.objects.get(id = id)
        context['classifieds'] = c

    return render(request, 'created.html', context)


#comentarios sobre clasificados
def comment(request):
    c = Classified.objects.get(id = request.POST.get('classifieds'))
    Comment.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        classified = c
    )
    return redirect('/classified')