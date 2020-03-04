from django.urls import path,include
from . import views
urlpatterns = [
    path('getbase',views.getBase,name='getbase'),
    path('getindex',views.getIndex,name='getindex'),
    path('getlogin',views.getlogin,name='getlogin'),
    path('getregister',views.getregister,name='getregister'),
    path('logout',views.logout,name='logout'),
    path('storybody',views.storybody,name='storybody'),
    path('captcha', include('captcha.urls')),
    path('publish',views.publish,name='publish'),
    path('forum',views.forum,name='forum'),
    path('forum_ajax',views.forum_ajax,name='forum_ajax'),

    path('sflogin',views.sflogin,name = 'sflogin'),
    #path('get_sflogin',views.get_sflogin,name = 'get_sflogin')

    path('comment',views.comment,name='comment'),

    path('message',views.message,name='message'),
    path('message_ajax',views.message_ajax,name='message_ajax'),
]