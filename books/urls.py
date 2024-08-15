from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.book_list, name='book_list'),
    url(r'new/', views.book_create, name='book_create'),
    url(r'^book/(?P<pk>[0-9]+)$', views.book_detail, name='book_detail'),
    url(r'^book/(?P<pk>[0-9]+)/edit$', views.book_update, name='book_update'),
    url(r'^book/<int:pk>/delete$', views.book_delete, name='book_delete'),
]
