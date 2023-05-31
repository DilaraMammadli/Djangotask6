from django.urls import path
from . import views



app_name = 'task6'

urlpatterns = [
    path('list/', views.infos, name="list"),
    path('detail/<id>', views.detail_view, name="detail"),
    path('create/', views.create_view, name = "create")
]

