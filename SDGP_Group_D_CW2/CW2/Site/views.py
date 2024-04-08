from django.http import HttpResponse
from django.template import loader

def Site(request):
  template = loader.get_template('graph-page.html')
  return HttpResponse(template.render())