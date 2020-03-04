from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class User_U(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


#文章
class  Post(models.Model):
    title = models.CharField(max_length=70)     #文章标题
    body = models.TextField()                   #文章内容
    created_time = models.DateTimeField()       #开始日期
    modified_time = models.DateTimeField()      #结束日期
    chuckle_k = models.BigIntegerField(max_length=70,default='')                #点赞
    order = models.IntegerField(blank=True, null=True, help_text="显示顺序")     #显示顺序
    author = models.ForeignKey(User,on_delete=models.CASCADE) #作者

    def __str__(self):
        return self.title

#评论
class Comment(models.Model):
    comment_body = models.TextField()       #评论内容
    comment_time = models.DateTimeField(auto_now=True)   #评论日期
    comment_title = models.ForeignKey(Post, on_delete=models.CASCADE)  # 评论标题
    comment_author = models.ForeignKey(User_U, on_delete=models.CASCADE) #评论者
    # def todict(self):
    #     return  {"comment_author": self.comment_author, "comment_time": self.comment_time,
    #                         'comment_body': self.comment_body}





#留言
class Message(models.Model):
    message_title = models.CharField(max_length=70) #留言标题
    message_body = models.TextField()               #留言内容
    message_time = models.DateTimeField(auto_now=True)           #留言日期
    message_author = models.ForeignKey(User_U, on_delete=models.CASCADE) #留言者

