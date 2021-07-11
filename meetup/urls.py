from meetup.ML.BGTs import BGTs
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('getData', views.getData, name='getData'),
    path('stop', views.stopCapture, name='stop'),
    path('run', views.runLiveCapture, name='runCapture'),
    path('<interface>', views.runTime, name='run'),

]
