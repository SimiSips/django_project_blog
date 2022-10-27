import datetime
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Book, Farm, Post, Comment
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, UserForm

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
	
@login_required(login_url='login')
def profile_view(request):
	return render(request, 'registration/profile.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration Successful.")
			return redirect("blog:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("blog:home")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("blog:home")

