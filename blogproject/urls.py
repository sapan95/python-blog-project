"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blog import views
from django.views.generic import ListView
from blog.models import Post
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list_view), #For function based
    path('tag/<str:tag_slug>/',views.post_list_view,name = 'tag_url'),
    #path('',views.PostListView.as_view()), #Class based view
    #path('',ListView.as_view(queryset = Post.objects.filter(status = 'published'),paginate_by = 3)),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail_view, name = 'post_detail'),
    path('<int:id>/share/',views.send_mail_view)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=path('__debug__/', include(debug_toolbar.urls)),