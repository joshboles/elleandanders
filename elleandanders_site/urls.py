from django.conf.urls.defaults import patterns, url
from django.conf import settings
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

def direct(request, path):    
    try:
        return render_to_response("%s.html" % path[:-1], context_instance=RequestContext(request))
    except:
        raise Http404

urlpatterns = patterns('',
    # Just for Development
    url(r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
    
    # My New Django Wiki-Alike Thing
    url(r"(?P<path>.*)", direct)
)