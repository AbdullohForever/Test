import random, io

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template

from .models import Question, Option, Answer

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape


@login_required
def question_list(request):
    questions = Question.objects.prefetch_related('option')[:5]

    for question in questions:
        options = list(question.option.all())
        random.shuffle(options)
        question.option.set(options)
    
    context = {'questions':questions}
    return render(request, 'main/test_questions.html', context)


@login_required
def submit_answers(request):
    if request.method == "POST":
        answers = {}
        true_answers_count = 0
        all_answers = Answer.objects.all()

        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('question_')[1]

                if all_answers.filter(question=question_id, option=value):
                    true_answers_count+= 1

        print("True answers:", true_answers_count)
        
        if true_answers_count >= 3:
            name = request.user.username
            pdfmetrics.registerFont(TTFont('AlexBrush', 'AlexBrush-Regular.ttf'))
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
            
            pdf = canvas.Canvas(response)
            pdf.setTitle('sample')
            pdf.setFont('AlexBrush', 36)
            pdf.drawCentredString(300, 770, 'Python course by Meta using Coursera')

            pdf.setFillColorRGB(0, 0, 255)
            pdf.setFont("Courier-Bold", 24) # Courier-Bold, AlexBrush
            pdf.drawCentredString(290, 720, name+' has passed successfully!')
            pdf.save()

            return response
        else:
            return HttpResponse("Not enough answers")
        return redirect('register')
    else:
        questions = Question.objects.prefetch_related('option')
        context = {'questions':questions}
        return render(request, 'submit_answers.html', context)

