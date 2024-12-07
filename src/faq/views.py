from django.views.generic import ListView

from faq.models import Question


class FAQView(ListView):
    model = Question
    template_name = "faq_list.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.prefetch_related("answers")
