from django.conf.urls import url
from stories.views import home, register, login

urlpatterns = [
   url(r'^$', home, name='home'),
   url(r'^register', register, name='register'),
   url(r'^login', login, name='login')
]
