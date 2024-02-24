from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index, name= "index"),
    path("<int:question_id>/", views.detail, name="details of id"),
    path('remove_vote/<int:choice_id>/', views.remove_vote, name='remove_vote'),
]
