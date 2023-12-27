from django.shortcuts import render, get_object_or_404, HttpResponse
from blog.models import Post
from datetime import datetime
from django.utils import timezone

# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(published_date__lt=timezone.now())
    filtered_post = posts.filter(status=True)
    context = {"posts": filtered_post}
    
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    if post.status == True:
        post.counted_view += 1
        post.save()
        try:
            next_post = Post.objects.filter(published_date__gt=post.published_date, status=True).order_by('published_date').first()
        except Post.DoesNotExist:
            next_post = None

        try:
            prev_post = Post.objects.filter(published_date__lt=post.published_date, status=True).order_by('-published_date').first()
        except Post.DoesNotExist:
            prev_post = None
        context = {'post': post, 'next_post': next_post, 'prev_post': prev_post}
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponse("This Post Is Not Published Yet!")
# a test for getting filter in db and make unique post
def test_with_time_and_published_date(request, pid):
    post = get_object_or_404(Post, pk=pid)
    current_time = timezone.now()
    if post.published_date <= current_time:
        post.counted_view += 1
        post.save()
        return render(request, 'test.html', {'post': post})
    else:
        return HttpResponse("Post Not Published")