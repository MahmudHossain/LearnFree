from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import author,category,article,events,subcategory,coursefaq,forumcomment
from django.contrib import admin
from .models import author,category,article,subcategory,events,comment,videolectures,videocomment

# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model=author
admin.site.register(author,authorModel)
class articleModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on","article_author"]
    search_fields = ["__str__"]
    list_per_page = 10
    list_filter = ["posted_on","category"]
    class Meta:
        Model=article
admin.site.register(article,articleModel)
class categotyModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=category
admin.site.register(category,categotyModel)
class subcategoryModel(admin.ModelAdmin):
    list_display = ["__str__","category"]
    search_fields = ["__str__","category"]
    list_per_page = 10
    class Meta:
        Model=subcategory
admin.site.register(subcategory,subcategoryModel)
class eventsModel(admin.ModelAdmin):
    list_display = ["__str__", "updated_on", "start_date","finish_date"]
    search_fields = ["__str__", "details"]
    list_per_page = 10
    list_filter = ["posted_on", "category"]

    class Meta:
        Model = events
admin.site.register(events,eventsModel)
class commentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=comment
admin.site.register(comment,commentModel)
class videolecturesModel(admin.ModelAdmin):
    list_display = ["__str__", "subcategory","posted_on"]
    list_filter = ["posted_on", "category"]
    list_per_page = 15
    search_fields = ["__str__", "subcategory"]
    class Meta:
        model=videolectures
admin.site.register(videolectures,videolecturesModel)
class videocommentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=videocomment
admin.site.register(videocomment,videocommentModel)
class coursefaqModel(admin.ModelAdmin):
    list_display = ["__str__","coursename"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=coursefaq
admin.site.register(coursefaq,coursefaqModel)
class forumcommentModel(admin.ModelAdmin):
    list_display = ["__str__",'content']
    search_fields = ["__str__"]
    list_filter = ["post"]
    list_per_page = 10
    class Meta:
        Model=forumcomment
admin.site.register(forumcomment,forumcommentModel)