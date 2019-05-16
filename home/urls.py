from django.urls import path
from . import views
from  django.contrib.auth import views as auth_views

app_name = 'home'
urlpatterns = [
    path('',views.index,name ='index'),
    path('(?P<album_id>[0-9]+)/details',views.details,name = 'details'),
    path('add_album',views.addAlbum,name = 'add_album'),
    path('(?P<album_id>[0-9]+)/add_song',views.addSong,name='add_song'),
    path('(?P<album_id>[0-9]+)/delete_album',views.deletAlbum,name='delete'),
    path('Signup',views.Users,name='singup'),
    #path('login',auth_views.LoginView.as_view(),name='login'),
    #path('logout',auth_views.LogoutView.as_view(),name='logout')
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),

]