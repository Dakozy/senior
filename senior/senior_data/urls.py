from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import SeniorListView, SeniorDetailView

LOGIN_URL = '/login/' 

urlpatterns = [
   path('', views.index_view, name='index'),
   path('list/', views.SeniorListView.as_view(), name='list'),
   path('searched/',  views.search_senior, name='searched'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('signup/', views.signup, name='signup'),
   path('add_senior/', views.add_senior, name='add_senior'),
   path('base', views.base, name='base'),
   #path('/detail/<int:pk>/', views.get_items, name='senior-detail'),
   path('senior/<slug:slug>/', SeniorDetailView.as_view(), name='senior-detail'),
   path('senior/<int:pk>/delete/', views.delete_senior, name='delete_senior'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

