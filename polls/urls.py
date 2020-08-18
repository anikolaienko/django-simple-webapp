from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('accounts/register', views.register, name='register')
]
