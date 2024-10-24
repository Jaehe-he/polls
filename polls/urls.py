from django.urls import path
from . import views

app_name = 'polls' #네임스페이스 설정

#config의 urls.py에 연결됨
urlpatterns=[
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'), #name이 index로 되어있고, polls로 끝나는 것만 뷰팅 되어있음

    #ex : /polls/5/   #5는 고정된 게 아니라 어떤 질문 선택하냐에 따라 다름 => <int:로 적어야함
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #ex : /polls/5/results,
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')

]

