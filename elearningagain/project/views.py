from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import author,article,category,events,comment,subcategory,videolectures,videocomment,coursefaq,forumcomment
from .forms import createForm,registerForm,createAtuhor,commentForm,videolecturesForm,videocommentForm,videolecturesForm,forumcommentForm
#from .models import Video
#from .forms import VideoForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    post = article.objects.all()
    first = article.objects.first()
    last = article.objects.last()
    subcat = subcategory.objects.all()
    contex = {
        "post": post,
        "first":first,
        "last":last,
        "subcat":subcat
    }
    return render(request,'index.html',contex)
def courses(request):
    coursecat = category.objects.all()
    subcat = subcategory.objects.all()
    subcatmenu = subcategory.objects.all()
    search = request.GET.get('q')
    if search:
        subcat = subcategory.objects.filter(
            Q(name__icontains=search)
            # Q(body__icontains=search)

        )
    post = events.objects.all()[:5]
    paginator = Paginator(subcat, 8)  # Show events per page
    page = request.GET.get('page')
    total_course = paginator.get_page(page)
    contex = {
        "coursecat": coursecat,
        "subcat": total_course,
        "post": post,
        "subcatmenu": subcatmenu
    }
    return render(request,'courses.html',contex)
def video(request):
    return render(request,'video.html')
def library(request):
    post = events.objects.all()
    first = events.objects.first()
    last = events.objects.last()
    paginator = Paginator(post, 6)  # Show events per page
    page = request.GET.get('page')
    total_article = paginator.get_page(page)

    contex = {
        "post": total_article,
        "first": first,
        "last": last,
    }
    return render(request,'library.html',contex)
def getevents(request,id):
    post = get_object_or_404(events, pk=id)
    first = events.objects.first()
    last = events.objects.last()
    related = events.objects.filter(category=post.category).exclude(id=id)[:4]
    contex = {
        "post": post,
        "first": first,
        "last": last,
        "related":related
    }
    return render(request,'event_details.html',contex)

def contact(request):
    return render(request,'contact.html')
def about(request):
    post=author.objects.all()
    contex={
        "post":post
    }
    return render(request,'about.html',contex)
def blog(request):
    post=article.objects.all()
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)|
            Q(body__icontains=search)

        )
    blogcat=category.objects.all()
    paginator = Paginator(post, 3)  # Show  posts per page

    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    search=request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )
    contex={
        "post":total_article,
        "blogcat":blogcat
    }
    return render(request,'blog.html',contex)
def gallery(request):
    post = events.objects.all()
    first = events.objects.first()
    last = events.objects.last()
    paginator = Paginator(post, 20)  # Show events per page
    page = request.GET.get('page')
    total_article = paginator.get_page(page)

    contex = {
        "post": total_article,
        "first": first,
        "last": last,
    }
    return render(request,'gallery.html',contex)
def blog_single(request,id):
    post=get_object_or_404(article,pk=id)
    first=article.objects.first()
    last=article.objects.last()
    getComment=comment.objects.filter(post=id)
    related=article.objects.filter(category=post.category).exclude(id=id)[:4]
    form=commentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post = post
        instance.save()
        return HttpResponseRedirect(reverse('blog_single', args=[id]))
    contex={
        "post":post,
        "first":first,
        "last":last,
        "related":related,
        "form":form,
        "comment":getComment
    }
    return render(request,'blog_single.html',contex)

def video_single(request,id):
    post=get_object_or_404(videolectures,pk=id)
    related = videolectures.objects.filter(category=post.category).exclude(id=id)[:4]
    first=videolectures.objects.first()
    last=videolectures.objects.last()
    getComment=videocomment.objects.filter(post=id)
    #related=article.objects.filter(category=post.category).exclude(id=id)[:4]
    form=videocommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post = post
        instance.save()
        return HttpResponseRedirect(reverse('video_single', args=[id]))
    contex={
        "post":post,
        "first":first,
        "last":last,
        "related":related,
        "form":form,
        "comment":getComment
    }
    return render(request,'video_single.html',contex)
    
def forum(request):
    subcat = subcategory.objects.all()
    contex={
        "subcat":subcat
    }
    return render(request,'forum.html',contex)

def getforum(request,name):
    subcat=get_object_or_404(subcategory,name=name)
    comments=forumcomment.objects.filter(post=subcat,reply=None).order_by('-time')
    if request.method == 'POST':
        form=forumcommentForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = forumcomment.objects.get(id=reply_id)
            comment=forumcomment.objects.create(post=subcat,content=content,reply=comment_qs)
            comment.save()
            form.save()
            return HttpResponseRedirect(reverse('forum',args=[name]))
    else:
        form=forumcommentForm()
    contex = {
        "subcat": subcat,
        "comments": comments,
        "form": form
    }
    return render(request,'courseforum.html',contex)
def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'Missmacthed username or password.')
                return render(request, 'login.html')

        return render(request,'login.html')
def getlogout(request):
    logout(request)
    return redirect('index')
def getcreate(request):
   if request.user.is_authenticated:
       u=get_object_or_404(author,name=request.user.id)
       form = createForm(request.POST or None, request.FILES or None)
       if form.is_valid():
           instance = form.save(commit=False)
           instance.article_author=u
           instance.save()
           return redirect('index')
       return render(request, 'create.html', {"form": form})
   else:
       return redirect('login')
def getauthor(request,name):
    #post_author = get_object_or_404(User, username=name)
    #auth=get_object_or_404(author,name=post_author.id)
    #post=article.objects.filter(article_author=auth.id)



    return render(request,'author.html')
def authorpage(request):
    return render(request,'author.html')
def getprofile(request):
    if request.user.is_authenticated:
        user=get_object_or_404(User,id=request.user.id)
        author_profile=author.objects.filter(name=user.id)
        if author_profile:
            author_user=get_object_or_404(author,name=request.user.id)
            post=article.objects.filter(article_author=author_user.id)
            return render(request,'profile.html',{"post":post,"user":author_user})
        else:
            form=createAtuhor(request.POST or None,request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name=user
                instance.save()
                redirect('profile')
            return render(request,'createauthor.html',{"form":form})

def getupdate(request,pid):
   if request.user.is_authenticated:
       u=get_object_or_404(author,name=request.user.id)
       post=get_object_or_404(article,id=pid)
       form = createForm(request.POST or None, request.FILES or None,instance=post)
       if form.is_valid():
           instance = form.save(commit=False)
           instance.article_author=u
           instance.save()
           messages.success(request, 'Update Successfull')
           return redirect('profile')
       return render(request, 'create.html', {"form": form})
   else:
       return redirect('login')
def getdelete(request,pid):
   if request.user.is_authenticated:
       post=get_object_or_404(article,id=pid)
       post.delete()
       messages.success(request, 'Delete Successfull')
       return redirect('profile')
   else:
       return redirect('login')
def getregister(request):
    form=registerForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,'Registration Completed Successfully')
        return redirect('login')
    return render(request,'register.html',{"form":form})
def getcategory(request):
    query=category.objects.all()
    return render(request,'category.html',{"query":query})
def gettopic(request,name):
    cat=get_object_or_404(category,name=name)
    post=article.objects.filter(category=cat.id)
    return render(request,'category.html',{"post":post})
def getlecture(request,name):
    cat=get_object_or_404(subcategory,name=name)
    post=videolectures.objects.filter(subcategory=cat.id)
    searchvideo=videolectures.objects.all()
    subcat = subcategory.objects.all()
    faq = coursefaq.objects.filter(coursename=cat.id)
    paginator = Paginator(post, 4)  # Show  posts per page

    page = request.GET.get('page')
    total_video = paginator.get_page(page)
    search = request.GET.get('q')
    if search:
        searchvideo = searchvideo.filter(
            Q(title__icontains=search)
        )
    contex = {
        "cat": cat,
        "post":total_video,
        "subcat":subcat,
        "searchvideo":searchvideo,
        "faq":faq
    }
    return render(request,'videolectures.html',contex)
def model_form_upload(request):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        form = videolecturesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.video_author = u
            instance.save()
            return redirect('index')
        return render(request, 'uploadvideo.html', {"form": form})
    else:
        return redirect('login')
