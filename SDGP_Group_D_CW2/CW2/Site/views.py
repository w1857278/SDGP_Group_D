from django.http import HttpResponse
from django.template import loader

def graph_page(request):
  template = loader.get_template('graph-page.html')
  return HttpResponse(template.render())
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())