from django.urls import path
from . import views

urlpatterns = [

    # Topic Section 
    path('', views.ListTopicsView, name='list_topics'),
    path('topic/create/', views.CreateTopicView, name='create_topic'),
    path('topic/update/<int:id>/', views.UpdateTopicView, name='update_topic'),
    path('topic/delete/<int:pk>/', views.delete_todo, name='delete_topic'),

    #  Points / Todo Section
    path('topic/<int:topic_id>/points/', views.ListPointsView, name='list_points'),
    path('topic/<int:topic_id>/points/add/', views.AddPointView, name='add_point'),
    path('points/update/<int:pk>/', views.UpdatePointView, name='update_point'),
    path('points/delete/<int:pk>/', views.DeletePointView, name='delete_point'),

    # AI Meaning Section 
    path('ai/ask/', views.AskMeaningView, name='ask_meaning'),
    path('ai/history/', views.MeaningHistoryView, name='meaning_history'),
    path('ai/result/<int:id>/', views.MeaningResultView, name='meaning_result'),
    path('ai/delete/<int:id>/', views.delete, name='delete_meaning'),
    path('ai/delete_all/', views.DeleteAll, name='delete_all_meanings'),

]
