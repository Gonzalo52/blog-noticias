from django.http import JsonResponse
from ..models import Post, Classified, Comment


def routes(request):
    routes = [
        'GET /api/posts',
        'GET /api/post/:id'
    ]
    return JsonResponse(routes, safe = False)


def posts(request):
    posts = Post.objects.all()
    posts_dict = []
    for p in posts:
        posts_dict.append({
            'title': p.title,
            'description': p.description,
            'id': p.id
        })
    return JsonResponse(posts_dict, safe = False)


def post(request, id):
    post = Post.objects.get(id = id)
    post_dict = {
        'title': post.title,
        'description': post.description,
        'text': post.text,
        'id': post.id
    }
    return JsonResponse(post_dict, safe = False)


def classifieds(request):
    classifieds = Classified.objects.all()
    classifieds_dict = []
    for c in classifieds:
        classifieds_dict.append({
            'title': c.title,
            'text': c.text,
            'id': c.id
        })
    return JsonResponse(classifieds_dict, safe = False)


def classified(request, id):
    classified = Classified.objects.get(id = id)
    classified_dict = {
        'title': classified.title,
        'text': classified.text,
    }
    return JsonResponse(classified_dict, safe = False)