from django.conf.urls import url
from webapp import views
urlpatterns = [
    url(r'^$',views.login_page,name = 'login'),
    url(r'^home/$',views.home_page,name = 'home'),
]
