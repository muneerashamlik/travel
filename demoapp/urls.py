from . import views
from django.urls import path

urlpatterns = [
     path('',views.demo,name='demo'),
     path('cute/',views.cutes,name='cutes')
    # path('add/',views.addition,name='addition'),
     #path('diff/',views.difference,name='difference'),
     #path('mul/',views.multiplication,name='multiplication'),
     #path('div/', views.division, name='division'),









     #path('', views.demo, name='demo'),
    #path('',views.home,name='home'),
    #path('about/',views.about,name='about'),
   # path('contact/',views.contact,name='contact'),
   # path('detail/',views.detail,name='detail'),
    #path('thanks/',views.thanks,name='thanks')

]