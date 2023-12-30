from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseForbidden
from blog.models import Post
from datetime import datetime
from django.utils import timezone

# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(published_date__lt=timezone.now(), status=True)
    context = {"posts": posts}
    
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = Post.objects.get(id=pid)
    all_posts = Post.objects.filter(status='True', published_date__lt=timezone.now()).order_by('id')
    current_post_index = list(all_posts).index(post)
    next_post = None
    prev_post = None
    try:
        if current_post_index > 0:
            prev_post = all_posts[current_post_index - 1]
        
        if current_post_index < len(all_posts) - 1:
            next_post = all_posts[current_post_index + 1]
            post.counted_view += 1
            post.save()
            if post.published_date > timezone.now():
                return HttpResponseForbidden("This Post Is Not Published Yet!")
        context = {'post': post, 'next_post': next_post, 'prev_post': prev_post}
        return render(request, 'blog/blog-single.html', context)
    
    except Post.DoesNotExist:   
        return HttpResponse("This Post Is Not Published Yet!")