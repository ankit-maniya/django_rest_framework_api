"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.student_list),
    path('stuinfo/<int:pk>', views.student_details),
    path('student_fetch_by_id/', views.student_fetch_by_id),
    path('student_create/', views.student_create),
    path('student_insert/', views.student_insert),
    path('student_update/', views.student_update),
    path('student_delete/', views.student_delete),
]
