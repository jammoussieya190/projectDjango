# urls.py

from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views  

urlpatterns = [
  
  path('', views.index, name='index'),
  path('home/', views.home, name='home'),
     path('accounts/', include('django.contrib.auth.urls')),
     path('blog/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
  path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
  
 
 path('publication_listcl/', views.publication_listcl, name='publication_listcl'),
 path('logementcl/', views.logementcl, name='logementcl'),
 path('evenementscl/', views.evenementscl, name='evenementscl'),
 path('transportscl/', views.transport_listecl, name='transportscl'),
  path('stagecl/', views.stagecl, name='stagecl'),
 
 
 
   path('publication_list/', views.publication_list, name='publication_list'),
    path('add_publication/', views.add_publication, name='add_publication'),
    path('edit_publication/<int:pk>/', views.edit_publication, name='edit_publication'),
    path('publication/<int:pk>/delete/', views.delete_publication, name='delete_publication'),

 
 
 
 
 
 
    path('transports/', views.transport_list, name='transport_list'),
    path('transports/add/', views.add_transport, name='add_transport'),
    path('transports/<int:pk>/edit/', views.edit_transport, name='edit_transport'),
    path('transports/<int:pk>/', views.delete_transport, name='delete_transport'),

    
    
     path('logement/', views.logement, name='logement'),  # Vue pour afficher la liste des logements
    path('ajouter_logement/', views.ajouter_logement, name='ajouter_logement'),
    path('modifier_logement/<int:logement_id>/', views.modifier_logement, name='modifier_logement'),
    path('supprimer_logement/<int:logement_id>/', views.supprimer_logement, name='supprimer_logement'),

    path('transport/', views.transport, name='transport'),
    path('stage/', views.stage, name='stage'),
 
    path('add-stage-offer/', views.add_stage_offer, name='add_stage_offer'),
    path('edit-stage-offer/<int:offer_id>/', views.edit_stage_offer, name='edit_stage_offer'),
    path('delete-stage-offer/<int:offer_id>/', views.delete_stage_offer, name='delete_stage_offer'),

    
    path('evenements/', views.evenements, name='evenements'),
     path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
 path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('publications/', views.publications, name='publications'),
    path('register/', views.register, name='register'), 
  path('login/', auth_views.LoginView.as_view(), name='login'), 
  path('logout/', views.logout_view, name='logout'),
]