from django.shortcuts import render
from .models import Question
import random


def home(request):
    return render(request, "questions/home.html")


def random_question(request):
    category = request.GET.get("category")
    difficulty = request.GET.get("difficulty")

    questions = Question.objects.all()

    if category:
        questions = questions.filter(category=category)

    if difficulty:
        questions = questions.filter(difficulty=difficulty)

    questions = list(questions)

    if not questions:
        return render(request, "questions/no_questions.html")

    question = random.choice(questions)

    return render(
        request,
        "questions/random_question.html",
        {
            "question": question,
            "selected_category": category,
            "selected_difficulty": difficulty,
        }
    )