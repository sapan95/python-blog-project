from django.contrib import admin
from blog.models import Post,Comment
from django.contrib.auth.admin import User,UserAdmin
# Register your models here.
'''class UserAdmin(UserAdmin):
    list_display = ['id','username','email','first_name','last_name','is_staff']

admin.site.unregister(User)
admin.site.register(User,UserAdmin)'''

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish','created','updated','status']
    list_filter = ('status','created','publish','author')
    prepopulated_fields = {'slug':('title','status','author')}#datetime field is not taking(publish) and giving error for created(system taken)
    search_fields = ('title','body','author__username')# __primary key of auth_user table
    raw_id_fields = ('author',) #must be a foreign key or a many-to-many field
    date_hierarchy ='publish'
    ordering = ['status','publish']
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
     