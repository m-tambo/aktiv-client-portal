from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.q_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f'Currently viewing Question #{question_id}')


def results(request, question_id):
    response = f'Currently viewing the results of Question #{question_id}'
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f'Vote on Question #{question_id}')

