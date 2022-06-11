from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /adrs/5/
    path('adrs/<int:adr_id>/', views.get_adr, name='adr_detail'),
    # ex: /new_adr
    path('new_adr', views.get_adr, name='new_adr')
]