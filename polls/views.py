from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice #models.py에 있는 Question을 불러와줘야 오류 안남
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    """Return the last five piblished question."""
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     #return HttpResponse("Hello, world. You're at the polls index")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] #관리자 페이지에서 Question을 추가할 때마다 object에 추가됨
#     # output = ', '.join([q.question_text for q in latest_question_list]) #', ' : string으로 들어감    # question_text를 list로 만들어줌
#     # return HttpResponse(output)
#
#     # view(투표 목록 만듦)와 template(화면에 불러옴) 역할 나뉨
#     #template = loader.get_template('polls/index.html')
#     context = { #context : template에서 미리 만들어둔 목록을 전달할 때 context 변수로 묶어서 사용
#         'latest_question_list' : latest_question_list,
#     }
#     #return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id): #어떤 질문을 선택해서 들어왔는지 question_id로 구분)
#     #return HttpResponse("You're looking at question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question}) #context 함수는 polls/detail.html에서 쓸거임
#
# def results(request, question_id):
#     # response = HttpResponse("You're looking at the results of question %s." % question_id)
#     # return response #그냥 return HttpResponse(~~~) 적어도 됨. response로 따로 안받고
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question' : question})

def vote(request, question_id): #투표 기능..*
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'polls/detail.html', {
        'question':question,
        'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))