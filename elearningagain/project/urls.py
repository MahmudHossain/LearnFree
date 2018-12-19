"""elearningagain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name="index"),
    path('courses', views.courses, name="courses"),
    path('library', views.library, name="library"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('author', views.author, name="author"),
    path('video', views.video, name="video"),
    path('login', views.getlogin, name="login"),
    path('forum', views.forum, name="forum"),
    path('register', views.getregister, name="register"),
    path('logout', views.getlogout, name="logout"),
    path('profile', views.getprofile, name="profile"),
    path('create', views.getcreate, name="create"),
    path('article/<int:id>', views.blog_single, name="blog_single"),
    path('events/<int:id>', views.getevents, name="event_details"),
    path('author/<name>', views.getauthor, name="author"),
    path('update/<int:pid>', views.getupdate, name="update"),
    path('delete/<int:pid>', views.getdelete, name="delete"),
    path('delete/<int:pid>', views.getdelete, name="delete"),
    path('topics', views.getcategory, name="categories"),
    path('topic/<name>', views.gettopic, name="topic"),
    path('lecture/<name>', views.getlecture, name="lecture"),
    path('forum/<name>', views.getforum, name="forum"),
    path('uploadvideo', views.model_form_upload, name="uploadvideo"),
    path('video/<int:id>', views.video_single, name="video_single"),




]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)