
from django.contrib import admin
from django.urls import path, include

# from task6.views import infos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("task6.urls"))
]
