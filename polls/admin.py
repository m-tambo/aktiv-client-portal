from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    readonly_fields = ['votes']  # this makes votes readonly (only within the inline question view)


class QuestionAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question_text"]
    
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "was_published_recently", "pub_date"]
    list_filter = ["pub_date"]  # provides a quick filtering sidebar to the right
    search_fields = ["question_text"]  # provides search bar at the top


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
 