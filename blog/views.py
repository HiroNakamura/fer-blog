
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    ##posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    try:
        form = PostForm(request.POST)
        print "formulario: ",form
        post = form.save(commit=False)
        print "Usuario:",request.user
        #user = request.user
        #user = User()
        #user = User.objects.get(username=request.user)
        user = User.objects.get(username='admin')
        print "Usuario: ",user
        post.author = user
        post.published_date = timezone.now()
        post.save()
        print "Post guardado"
    except ValueError as error:
        print "Error al crear nuevo post: ",error
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print "Post:", post
    print "Autor:", post.author
    print "Titulo:", post.title
    print "Texto:", post.text
    print "Request:",request
    form = PostForm(request.POST, instance=post)
    valido = "Formulario valido" if form.is_valid() else "Formulario no valido"
    if request.method == "POST":
        print "form: ",form
        print valido
        if form.is_valid():
            print "Formulario valido"
            post = form.save(commit=False)
            #post.author = request.user
            user = User.objects.get(username='admin')
            print "Usuario: ",user
            post.author = user
            post.save()
            print "Post editado"
            return redirect('post_detail', pk=post.pk)
        else:
            print "form no valido"
            form = PostForm(instance=post)
    else:
        print "form: ",form
        print valido
        return render(request, 'blog/post_edit.html', {'form': form})


'''
def post_new(request):
    if request.method == "POST":
        try:
            form = PostForm(request.POST)
        except:
            print "A#-Ha ocurrido una excepcion al crear nuevo post" 
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
            except ValueError:
                print "B#-Ha ocurrido una excepcion al crear nuevo post"
            return redirect('post_detail', pk=post.pk)
        else:
            print "form no valido"
            try:
                form = PostForm()
            except:
                print "C#-Ha ocurrido una excepcion al crear nuevo post"
        return HttpResponseRedirect(reverse_lazy('blog/post_edit.html'))
        #return render(request, 'blog/post_edit.html', {'form': form})
        #return render(request, 'blog/post_edit.html',context_instance=RequestContext(request))
'''


'''
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
'''

'''
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect("post_detail",{"form":form})
            #return redirect('post_detail', pk=post.pk)      
        else:
            form = PostForm(instance=post)
        return render_to_response("blog/post_edit.html",{"form":form} , context_instance = RequestContext(request))
        #return render(request, 'blog/post_edit.html', {'form': form})
'''      

#return render(request, 'blog/post_edit.html',context_instance=RequestContext(request))
#return HttpResponseRedirect(reverse_lazy('adopcion:solicitud_listar'))
#return render(request, 'auth_lifecycle/user_profile.html',
#context_instance=RequestContext(request))