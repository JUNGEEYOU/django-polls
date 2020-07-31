from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
"""
 뷰 추가하기 
  - 투표 목록: 등록된 투표의 목록을 표시
  - 투표 상세: 투표의 상세 항목을 보여줌
  - 투표 기능: 선택한 답변을 반영 
  - 투표 결과: 선택한 답변을 반영 한 후 결과를 보여줌.
"""

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)   # 이는 try-except 구문을 없애고 간소화 가능 자동 404 처리
#     return render(request, 'polls/detail.html', {'question':question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)  # 이는 try-except 구문을 없애고 간소화 가능 자동 404 처리
#     return render(request, 'polls/results.html', {'question': question})

# 클래스형 뷰: generic 상속 받아 사용 -urls.py도 수정 필요
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))