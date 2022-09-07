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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views, views_drf, views_genericApi_mixin, views_genericApi_concrete, views_viewsets

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register(
    'studentapi', views_viewsets.StudentModelViewSet, basename='Student',
)

router.register(
    'studentapinew', views_viewsets.StudentModelViewSetCustome, basename='StudentNew'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.student_list),
    path('stuinfo/<int:pk>', views.student_details),
    path('student_fetch_by_id/', views.student_fetch_by_id),
    path('student_create/', views.student_create),
    path('student_insert/', views.student_insert),
    path('student_update/', views.student_update),
    path('student_delete/', views.student_delete),
    path('hello_word/<int:pk>', views_drf.hello_word),
    path('hello_word/', views_drf.hello_word),
    # path('studentapi/', views_genericApi_mixin.StudentList.as_view()),
    # path('studentapi/', views_genericApi_mixin.StudentCreate.as_view()),
    # path('studentapi/<int:pk>', views_genericApi_mixin.StudentRetrive.as_view()), # retrive single student
    # path('studentapi/<int:pk>/', views_genericApi_mixin.StudentUpdate.as_view()), # update single user
    # path('studentapi/<int:pk>/', views_genericApi_mixin.StudentDelete.as_view()),
    # path('studentapi/', views_genericApi_mixin.StudentListAndCreate.as_view()),
    # path('studentapi/<int:pk>/', views_genericApi_mixin.StudentRetriveUpdateAndDelete.as_view()),
    # path('studentapi/', views_genericApi_concrete.StudentList.as_view()),
    # path('studentapi/', views_genericApi_concrete.StudentCreate.as_view()),
    # path('studentapi/<int:pk>', views_genericApi_concrete.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>', views_genericApi_concrete.StudentUpdate.as_view()),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="Rest_Framework")),
]
