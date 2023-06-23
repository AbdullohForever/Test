import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import TimeStampedModel


class Question(TimeStampedModel):
    text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.id)+'.'+self.text
    
    class Meta:
        ordering = ['created_at']
        verbose_name = 'Savol'
        verbose_name_plural = '1.Savollar'


class Option(TimeStampedModel):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option')

    def __str__(self) -> str:
        return str(self.id)+'.'+self.text

    class Meta:
        ordering = ['created_at', 'text']
        verbose_name = 'Variant'
        verbose_name_plural = '2.Variantlar'


class Answer(TimeStampedModel):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Javob"
        verbose_name_plural = "3.Javoblar"


# 2-way
# class Test(models.Model):
#     question = models.CharField(max_length=255)

# class Option(models.Model):
#     text = models.CharField(max_length=255)
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)




# class Test(TimeStampedModel):
#     question = models.CharField(max_length=250, unique=True, verbose_name='Savol')
#     answer = models.CharField(max_length=250)
#     option1 = models.CharField(max_length=250)
#     option2 = models.CharField(max_length=250)
#     option3 = models.CharField(max_length=250)

#     def __str__(self):
#         return str(self.id)+'.'+self.question

#     class Meta:
#         ordering = ['question']
#         verbose_name = 'Test'
#         verbose_name_plural = 'Testlar'

#     def shuffle_options(self):
#         options = [self.answer, self.option1, self.option2, self.option3]
#         random.shuffle(options)
#         self.answer = options[0]
#         self.option1 = options[1]
#         self.option2 = options[2]
#         self.option3 = options[3]