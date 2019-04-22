from django.conf.urls import url
from stories.views import (
   home,
   register,
   login,
   create_article
)

urlpatterns = [
   url(r'^$', home, name='home'),
   url(r'^register', register, name='register'),
   url(r'^login', login, name='login'),
   url(r'^create_article', create_article, name='create_article')
]
