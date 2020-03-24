from django.conf.urls import url, include
from rest_framework import routers
from analyse.views import  AnalyseVideoView


router = routers.DefaultRouter()

urlpatterns = [
  url(r'^analyse_video', AnalyseVideoView.as_view()),
  url(r'', include(router.urls))
]
