"""django_crud_api URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import  crud_queryset.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',crud_queryset.views.homepage, name='home-page'),
    path('add_task',crud_queryset.views.add_task, name='add-task'),
    path('all_tasks',crud_queryset.views.all_tasks_list, name='all-tasks'),
    path('task/<int:pk>',crud_queryset.views.view_task,name='detail'),
    path('task/<int:pk>/update', crud_queryset.views.update_task, name='update-task'),
    path('task/<int:pk>/delete', crud_queryset.views.delete_task, name='delete-task'),
    path('search_everything', crud_queryset.views.search_everything, name='search-site'),
]
 