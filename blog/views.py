from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from time import strftime

from .models import About, Blog, Comment

def about(request):
    return render(request,
        'blog/about.html', 
        {
            'now': strftime('%c'),
        }
    )

def tips(request):
    return render(request,
        'blog/techtips+css.html', 
        {
            'now': strftime('%c'),
        }
    )

def home(request):

    blogPosts = Blog.objects.order_by('-posted')[:3]

    return render(request,
        'blog/bloghome.html',
        {
            'blogPosts': blogPosts
        }
    )

def archive(request):

    blogPosts = Blog.objects.order_by('-posted')

    return render(request,
        'blog/blogarchive.html',
        {
            'blogPosts': blogPosts
        }
    )

def entry(request, blog_id):
    blogPost = get_object_or_404(Blog, pk=blog_id)

    return render(request,
        'blog/blogentry.html',
        {
            'blogPost': blogPost
        }
    )

def addcomment(request, blog_id):
    blogPost = get_object_or_404(Blog, pk=blog_id)

    try:    
        comment = blogPost.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        return(render(request,
                'blog/addcomment.html',
                {
                    'blogPost': blogPost,
                }
            )
        )
    else:
        comment.posted = timezone.now()
        comment.save()
        return HttpResponseRedirect(reverse('blog:entry', args=(blogPost.id,)))