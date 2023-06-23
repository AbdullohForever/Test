from django.urls import path
from main.views import question_list, submit_answers

urlpatterns = [
    path(route='test/', view = question_list, name='question-list'),   
    path('submit-answers', submit_answers, name='submit_answers')

]