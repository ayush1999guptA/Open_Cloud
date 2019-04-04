from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView ,View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import UserForm,LoginForm
from .models import Album,Song

# ====================Album===============
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')
# ====================================User========================================
class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):

        form = self.form_class(None)

        return render(request, self.template_name,{ 'form':form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()


            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('index')



        else:
            return render(request, self.template_name, {'form': form})


def LogOut(request):
    form=LoginForm(None)
    logout(request)
    return render(request,'music/login.html',{'form':form})


class UserLogin(View):

    form_class=LoginForm

    template_name='music/login.html'

    def get(self,request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self,request):
            form = self.form_class(None)
            username = request.POST['username']
            password = request.POST['password']

            user=authenticate(username=username,password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')
            else:
                return render(request, self.template_name, {'form': form})

# ===============================song============================

class SongsIndex(generic.ListView):

    template_name = 'music/song_index.html'
    context_object_name = 'all_music'

    def get_queryset(self):
        return Song.objects.all()


class SongCreate(CreateView):
    model = Song
    fields = ['album','file_type','song_title','song_file']

class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'song_file']


