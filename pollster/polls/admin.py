from django.contrib import admin

# Register your models here.
# this is what enables editing in admin UI
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
