from django.conf.urls import url
from stories import views

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^register', views.register, name='register'),
   url(r'^login', views.login, name='login'),
   url(r'^create_article', views.create_article, name='create_article'),
   url(r'^get_home', views.index, name='index')
]
