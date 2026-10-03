from django.shortcuts import render
from .models import Question
import random


def random_question(request):
    questions = list(Question.objects.all())

    if not questions:
        return render(request, "questions/no_questions.html")

    question = random.choice(questions)

    return render(
        request,
        "questions/random_question.html",
        {"question": question}
    )
