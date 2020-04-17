from django.urls import path
from . import views

app_name = 'datasets'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_index>', views.page, name='page'),
    path('<str:path_name>/<int:page_index>', views.path_page, name='path_page'),
    path('<int:id>/details', views.details, name='details'),
    path('create', views.create, name='create'),
]
