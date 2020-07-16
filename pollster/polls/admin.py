from django.contrib import admin

# Register your models here.
# this is what enables editing in admin UI
from .models import Question, Choice
admin.site.site_header = "Pollster Admin"
admin.site.site_header = "Pollster Admin Area"
admin.site.site_header = "Welcome to the Pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': [
                  'pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
