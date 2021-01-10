from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('sample-page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))
