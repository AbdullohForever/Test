import random, io

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import Question, Option, Answer

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.template.loader import get_template


# def generate_pdf(name):
#     print("Generating pdf file")
#     pdf = canvas.Canvas("example.pdf", pagesize=letter)
#     pdf.setFont("Helvetica", 12)
#     pdf.drawString(100, 750, f"Hello, {name}")
#     pdf.drawString(100, 700, "This is example PDF document created using python")
#     pdf.save()
    

@login_required
def question_list(request):
    questions = Question.objects.prefetch_related('option')[:5]
    # print("Len: ", len(questions))

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
                # answers[question_id] = value
                if all_answers.filter(question=question_id, option=value):
                    true_answers_count+= 1

        print("True answers:", true_answers_count)
        
        if true_answers_count >= 3:
            print("generating certificate new!")
            name = request.user.username
            template = get_template('main/certificate.html')
            certificate_data = {
                'name':name,
            }
            rendered_template = template.render(certificate_data)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer)
            pdf.drawString(100, 750, rendered_template)
            pdf.showPage()
            pdf.save()
            pdf_data = buffer.getvalue()
            buffer.close()
            response.write(pdf_data)
            return response
        else:
            return HttpResponse(request, "Not enough answers")
        return redirect('register')
    else:
        questions = Question.objects.prefetch_related('option')
        context = {'questions':questions}
        return render(request, 'submit_answers.html', context)









# class TestView(ListView):
#     model = 
#     template_name = 'main/test_questions.html'
#     context_object_name = 'tests'

#     def get_queryset(self):
#         all_tests = Test.objects.all()
#         random_tests = random.sample(list(all_tests), 10)
#         return random_tests
    