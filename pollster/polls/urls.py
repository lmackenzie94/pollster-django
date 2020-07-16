from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # empty string refers to 'polls/' because..
    # path('polls/', include('polls.urls')) in pollster > urls.py

    path('', views.index, name="index"),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
]
