from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement', {'fields' : ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes' : ['collapse']})
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin) #admin 사이트에 Question 테이블을 관리할 수 있도록 됨
admin.site.register(Choice)