from django.urls import path

from blog import views


urlpatterns = [
 path('blog/', views.blog.as_view(), name='blog'),
 
]