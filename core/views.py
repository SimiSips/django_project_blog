import datetime
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Book, Farm, Post, Comment
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


# Create your views here.

def displayTime(request):
    now = datetime.datetime.now()
    text = "The time is {}".format(now)
    return HttpResponse(text)

def farm_view(request):
    farm = Farm.objects.all()
    return render(request, 'farm.html', {'farm_data': farm})

def home_view(request):
    post_list = Post.objects.all()
    #comments = Comment.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = Paginator.page(paginator.num_pages)

    book_list = Book.objects.all()
    
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'home.html', {'user': users, 'books':book_list, 'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            comment_form.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})