from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         password = request.POST['password']
         r_password = request.POST['repeat_password']
         if password != r_password:
             return render(request, 'Core/auth/signup.html', {
                 'error': 'Пароли не совпадают.'
             })
         User.objects.create_user(
             username=username, 
             email=email,
             password=password,
         )
         return redirect('signin')
    return render(request, 'Core/auth/signup.html')
 
def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, username=username, password=password
        )
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'Core/auth/signin.html', {
                'error': 'Неверный логин или пароль.'
            })
    return render(request, 'Core/auth/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'Core/auth/profile.html')

def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'Core/createPost.html', {'form': form})

def posts(request):
    posts = Post.objects.filter(is_hidden=False)
    return render(request, 'Core/posts.html', {'posts': posts})

def subs_posts(request):
    posts = Post.objects.filter(is_hidden=False)
    posts_actual = []
    subs_list = []
    subs = request.user.subscriptions.all()
    for sub in subs:
        subs_list.append(sub.username)
    for post in posts:
        if post.author.username in subs_list:
            posts_actual.append(post)
    return render(request, 'Core/subs_posts.html', {'posts': posts_actual})

def request_posts(request):
    posts = Post.objects.filter(is_hidden=True)
    return render(request, 'Core/request_posts.html', {'posts': posts})

def profile_list(request):
    profile_list = User.objects.all()
    subs_list = []
    subs = request.user.subscriptions.all()
    for sub in subs:
        subs_list.append(sub.username)
    return render(request, 'Core/auth/profile_list.html', {'profile_list': profile_list, 'subs_list': subs_list})

def add_post_comment(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        PostComment.objects.create(
            author=request.user,
            text=request.POST.get('comment_text'),
            post=Post.objects.get(id=post_id)
        )
        return redirect('posts')

def action_subscriptions(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=request.user.id)
        sub = User.objects.get(id=user_id)
        action = request.POST.get('action')
        if action == 'add':
            user.subscriptions.add(sub)
        else:
            user.subscriptions.remove(sub)
        return redirect('profile_list')

def tags_list(request):  
    tags = Tag.objects.all()
    print(tags)
    return render(request, 'Core/tags_list.html', {
        'tags': tags
    })

def tags_detail(request, tage_id): 
    tag = Tag.objects.get(id=tage_id)

    posts = tag.posts.all()
    return render(request, 'Core/tags_detail.html', {
        'tag': tag, 'posts': posts
    })
