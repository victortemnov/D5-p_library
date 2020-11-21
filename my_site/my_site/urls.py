from django.contrib import admin
from django.urls import include, path

from p_library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publishers_list),
]
