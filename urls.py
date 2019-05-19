from django.conf.urls import url
from mpapp import views

app_name = 'mpapp'

urlpatterns = [
url(r'^$',views.Home,name='Home'),
url(r'^create/$',views.create,name='create'),
url(r'^questions/$',views.questions,name='questions'),
url(r'^show/$',views.show,name='show'),
url(r'^map/$',views.map,name='map'),
]
