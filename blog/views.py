from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag

def blog_home(request):
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)