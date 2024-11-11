from django.contrib import admin

from faq.models import Question, Answer

admin.site.register([Question, Answer])
