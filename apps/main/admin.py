from django.contrib import admin
from main.models import Question, Option, Answer

@admin.register(Question)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    search_fields = ('text', )
    list_filter = ('text', )
    ordering = ['text',]


@admin.register(Option)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question')
    list_display_links = ('id', 'text', 'question')
    search_fields = ('text', )
    list_filter = ('question', )
    ordering = ['text',]


@admin.register(Answer)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'option')
    list_display_links = ('id', 'question', 'option')
    list_filter = ('question',)
    