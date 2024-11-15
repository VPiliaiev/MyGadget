from django.contrib import admin

from faq.models import Answer, Question

admin.site.register([Question, Answer])
