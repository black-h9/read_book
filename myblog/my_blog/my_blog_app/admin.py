from django.contrib import admin
from . import models


# Register your models here.
class User_UAdmin(admin.ModelAdmin):
    list_display = ['id','name','password','email','sex','c_time']

class Post_Admin(admin.ModelAdmin):
    list_display = ['id','title','created_time','modified_time','chuckle_k','order','author']

class Comment_Admin(admin.ModelAdmin):
    list_display = ['id','comment_time','comment_title','comment_author']


class Message_Admin(admin.ModelAdmin):
    list_display = ['id','message_title','message_time','message_author']


admin.site.register(models.User_U,User_UAdmin)
admin.site.register(models.Post,Post_Admin)
admin.site.register(models.Comment,Comment_Admin)
admin.site.register(models.Message,Message_Admin)