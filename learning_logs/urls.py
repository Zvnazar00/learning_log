""" Визначає регулярні вирази URL для learning_logs"""
"""Defines URL pattern for learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # Сторінка присвячена окремій темі
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]