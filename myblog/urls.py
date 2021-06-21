"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="home"),
    path('posts', views.posts, name="posts"),
    # path(' post_list', views.post_list, name= " post_list"),
    path('post_detail/<int:pk>/', views.post_detail, name="post_detail"),
    
    path('post_update/<int:pk>/post_update/',
         views.post_update, name="post_update"),
    
    path('post_detail/<int:pk>/post_delete/',
         views.post_delete, name="post_delete"),
    
    path('search_results', views.search_results, name="search_results"),

    path('post_create/', views.post_create, name="post_create"),
#     path('post_update', views.search_results, name="post_update"),
#     path('post_delete', views.search_results, name="post_delete")
 ]

# path('search_results/', views.search_results, name="search_results"),
# path('post_create/', views.post_create, name="post_create"),
# path('post/<int:pk>/', views.post, name='post-detail'),
# path('post/<int:pk>/update/', views.post_update, name='post_update'),
# path('post/<int:pk>/delete/', views.post_delete, name='post_delete')
