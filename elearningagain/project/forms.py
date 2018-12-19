from django import forms
from .models import article,author,comment,videolectures,videocomment,forumcomment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class createForm(forms.ModelForm):
    class Meta:
        model=article
        fields=[
            'title',
            'body',
            'image',
            'category'
        ]
class registerForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'

        ]
class createAtuhor(forms.ModelForm):
    class Meta:
        model=author
        fields=[
            'profile_pic',
            'details',
        ]
class commentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=[
            'name',
            'email',
            'post_comment'
        ]
class videolecturesForm(forms.ModelForm):
    class Meta:
        model=videolectures
        fields = [
            'title',
            'description',
            'video_file',
            'document',
            'subcategory',
            'category',
        ]
class videocommentForm(forms.ModelForm):
    class Meta:
        model=videocomment
        fields=[
            'name',
            'email',
            'post_comment'
        ]
class forumcommentForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'', 'rows':4, 'col':50}))
    class Meta:
        model=forumcomment
        fields=[
            'content'
        ]