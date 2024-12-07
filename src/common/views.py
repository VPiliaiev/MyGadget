from django.views.generic import TemplateView

from mygadget.models import ProductCategory


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.filter(parent=None)
        return context
