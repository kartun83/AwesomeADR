from django.urls import path

from . import views
from .views import ADRListView


urlpatterns = [
    path('', ADRListView.as_view()),
    # ex: /adrs/5/
    path('adrs/<int:adr_id>/', views.get_adr, name='adr_detail'),
    # ex: /new_adr
    path('new_adr', views.get_adr, name='new_adr'),
    path('gen_overview', views.gen_overview, name='overview'),
]