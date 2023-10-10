from django.contrib import admin

from . import models
from .models import Rating, Question, Profession, Answer, VideoAnswerLink, ExtraContentLink, MockInterview

admin.site.register(models.Tag)


@admin.register(MockInterview)
class MockInterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'profession', 'public', 'created_at', 'grade')
    search_fields = ('title',)


@admin.register(ExtraContentLink)
class ExtraContentLinkAdmin(admin.ModelAdmin):
    list_display = ('question', 'title', 'public', 'created_at')


@admin.register(VideoAnswerLink)
class VideoAnswerLinkAdmin(admin.ModelAdmin):
    list_display = ('question', 'title', 'public', 'created_at')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'public', 'created_at')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'public_rating', 'public_mock', 'public_analytic', 'votes', 'votes_access')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('question', 'profession', 'rating', 'position', 'public', 'created_at')
    search_fields = ('question__title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag', 'grade', 'created_at')
    search_fields = ('title',)