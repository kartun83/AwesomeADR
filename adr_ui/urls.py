from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /adrs/5/
    path('adr_ui/adrs/<int:adr_id>/', views.adr_detail, name='adr_detail'),
    # ex: /new_adr
    path('adr_ui/new_adr', views.new_adr, name='new_adr')
]