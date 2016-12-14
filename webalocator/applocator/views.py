from django.views.generic.base import TemplateView


class MapLocationView(TemplateView):
    template_name="maplocation.html"

# 1. from django.http import HttpResponse


# 1. def home(request):
# 1.    return HttpResponse("hello, world")

# http://maps.google.com/?q=-47.4525603,-23.5015299 
# http://www.google.com/maps/place/-23.5015299, -47.4525603 
