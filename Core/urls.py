from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),
    path("createPost/", createPost, name="createPost"),
    path("posts/", posts, name="posts"),
    path("subs_posts/", subs_posts, name="subs_posts"),
    path("request_posts/", request_posts, name="request_posts"),
    path("profiles/", profile_list, name="profile_list"),
    path('add_post_comment/', add_post_comment, name='add_post_comment'),
    path('action_subscriptions/', action_subscriptions, name='action_subscriptions'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<int:tage_id>/', tags_detail, name='tags_detail'), 
]