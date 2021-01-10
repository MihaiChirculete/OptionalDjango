from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"
