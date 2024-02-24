from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})


def remove_vote(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.remove_vote()
    return render(request, "result.html", {"choice":choice})