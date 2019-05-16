from django.shortcuts import render,get_object_or_404,redirect
from .models import Album
from .forms import Form,SongForm,UserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='home:login')
def index(request):
    albums = Album.objects.filter(user=request.user)
    context = {
        'albums': albums
    }
    return render(request,'home/index.html',context)

def details(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'home/details.html',{'album':album})

@login_required(login_url='home:login')
def addAlbum(request):
    form = Form(request.POST or  None,
                request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.user=request.user
        album.cover = request.FILES['cover']
        album.save()
        return  render(request, 'home/details.html',{'album':album})
    return render(request,'home/add_album.html',{'form':form})

def addSong(request,album_id):
    form= SongForm(request.POST or None,request.FILES or None)
    album = get_object_or_404(Album ,pk=album_id)
    if form.is_valid():
        save_song = form.save(commit=False)
        save_song.audio=request.FILES['audio']
        save_song.album=album
        save_song.save()
        return  render(request,'home/details.html',{'album':album})
    return render(request,'home/add_song.html',{'form':form})

def deletAlbum(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    album.delete()
    return  redirect('home:index')

def Users(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username =form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user=authenticate(username=username,
                          password=password)
        login(request,user)
        return redirect('home:index')
    return  render(request,'home/signup.html',
                   {'form':form})

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('home:index')

    return render(request,'registration/login.html')
def logout_user(request):
    logout(request)
    return redirect('home:login')