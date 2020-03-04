from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm
from .forms import RegisterForm
# from .forms import ListForm
# from  .forms import PublishForm
from django.http import JsonResponse
from . import models
import hashlib
import datetime
# Create your views here.
def getBase(request):

    return render(request,'blog/base.html')
def getIndex(request):
    # text = ListForm()
    # titles = models.Post.objects.all()
    return render(request,'blog/index.html',)

def getlogin(request):
    if request.session.get('is_login', None):
        return redirect('/blog/getindex')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User_U.objects.get(name=username)
                if user.password == hash_code(password):
                # if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/blog/getindex')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'blog/login.html', locals())

    login_form = UserForm()
    return render(request, 'blog/login.html', locals())


def getregister(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/blog/getindex/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'blog/register.html', locals())
            else:
                same_name_user = models.User_U.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'blog/register.html', locals())
                same_email_user = models.User_U.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'blog/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User_U.objects.create()
                new_user.name = username
                # new_user.password = password1
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/blog/getlogin')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'blog/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/blog/getindex")
    request.session.flush()
    return redirect("/blog/getindex")

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def storybody(request):
     pass


def publish(request):
    messages = models.Message.objects.all()
    return render(request, 'blog/publish.html',locals())

def message(request):
    id = request.GET.get('id')
    message_body =models.Message.objects.get(id=id)
    body=message_body.message_body
    print(body)

    return JsonResponse({'btn':body})

def message_ajax(request):
    ''' 1.先检测是否登陆
        2.提取登陆的id
        3.获取提交的内容
        4.保存'''
    if request.session.get('is_login', None):


        comment_author = request.session['user_name']

        id = models.User_U.objects.get(name=comment_author)#留言id
        message_title = request.GET.get('title')           #留言标题
        message_body = request.GET.get('body')
        print(id.id)#留言内容

    else:
        return JsonResponse({'btn':'登陆后才能留言'})
    sql = models.Message(
    message_title = message_title,
    message_body = message_body,
    message_author = id)
    sql.save()

    return JsonResponse({'btn':'你已经成功留言，记得查看'})


def forum(request):
    post = models.Post.objects.all()
    return render(request,'blog/forum.html',locals())

def forum_ajax(request):
    id = request.GET.get('id')
    body = models.Post.objects.get(id=id)
    comment_QuerySet = models.Comment.objects.filter(comment_title=body)


    pop = []
    for x in comment_QuerySet:
        pl3 = x.comment_author   #评论作者
        pl= x.comment_body       #评论内容
        pl2= x.comment_time      #评论时间
        # print(pl2.strftime('%Y-%m-%d %H:%M:%S'))
        pl2_p = pl2.strftime('%Y-%m-%d %H:%M')
        pl_pl = str(pl3)+':'+pl +str(pl2_p)
        pop.append(pl_pl)

    for xx in pop:
        print(xx)


    return JsonResponse({'body':body.body,'pls':pop})



#提交评论
def comment(request):
    if request.session.get('is_login', None):
        comment_author = request.session['user_name']
        print(comment_author)
        tar = request.GET.get('tar')
        id = request.GET.get('id')

    else:
        return JsonResponse({'bk':'亲！登陆后才能评论哦,哈哈'})


    m=models.Comment.objects.create()
    m.comment_author=comment_author
    m.comment_body =tar
    body = models.Post.objects.get(id=id)
    comment_title =body.title
    m.comment_title =comment_title

    return render(request, 'blog/forum.html', )


#评论内容，时间，评论的作者，评论标题
def sflogin(request):
    '''设置session request.session.get('is_login', None):'''

    if request.session.get('is_login', None):
        post_id=request.POST.get("id")
        comment_title=models.Post.objects.get(id=post_id)
        comment_body=request.POST.get("comment_body")
        user_name = request.session['user_name']
        comment_author = models.User_U.objects.get(name=user_name)
        comment=models.Comment.objects.create(
            comment_title=comment_title,comment_body=comment_body,comment_author=comment_author
        )
        comment.save()


    else:
        return JsonResponse({'bk':'先登陆'})
    return JsonResponse({'bk':'亲！评论已成功'})


def ck(request):

    pass
