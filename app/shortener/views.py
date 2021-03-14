from django.shortcuts import get_object_or_404
from app.shortener.models import Shortener
from django.views.generic import TemplateView


# Create your views here.
class RedirectView(TemplateView):
    template_name = "app/shortener/redirect.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Shortener, alias=kwargs.get('alias'))
        obj.source_set.create(reference="https://www.google.com")
        obj.location_set.create(locale="id")
        obj.statistic_set.create()
        obj.increment()
        context["shortener"] = obj
        context["timeout"] = 3000
        return context
    