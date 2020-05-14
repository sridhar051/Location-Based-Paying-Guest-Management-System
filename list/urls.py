from django.urls import path
from . import views

urlpatterns = [
    path('pglist',views.pglist,name='pglist'),
    path('pglists',views.pglists,name='pglists'),
    path('map',views.map,name='map'),
    path('pay',views.pay,name='pay'),
]
