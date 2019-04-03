from django.conf.urls import url
from MyApp import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view()),
]