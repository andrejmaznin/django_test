from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:id>/', views.news_id),
    path('add/', views.add),
    path('stats/', views.stats)

]
