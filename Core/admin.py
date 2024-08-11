from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_editable = ('email',)