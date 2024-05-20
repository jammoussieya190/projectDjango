
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from HelpStudent import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
   path('HelpStudent/', include('HelpStudent.urls')),
   path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Utilisez la vue register de votre application magasin
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
