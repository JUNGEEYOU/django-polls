from django.urls import path
from . import views

app_name = 'polls'

# 각 route에 연결할 view를 넣어줍니다.
# <>는 변수를 의미합니다.
urlpatterns =[
    # path('', views.index, name='index'),                                # /polls/
    # path('<int:question_id>/', views.detail, name='detail'),            # /polls/5
    # path('<int:question_id>/results', views.results, name='results'),   # /polls/5/results
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),            # /polls/5/vote

]