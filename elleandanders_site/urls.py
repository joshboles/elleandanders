from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib import admin
admin.autodiscover()

def direct(request, path):    
    try:
        return render_to_response("%s.html" % path[:-1], context_instance=RequestContext(request))
    except:
        raise Http404

urlpatterns = patterns('',
	url(r"^admin/", include(admin.site.urls)),
    url(r"^rsvp/", "rsvp.views.rsvp", name="rsvp"),

    # Just for Development
    url(r"^site_media/static/(?P<path>.*)$", "django.contrib.staticfiles.views.serve", {"document_root": settings.STATIC_ROOT}),
    
    # My New Django Wiki-Alike Thing
    url(r"(?P<path>.*)", direct)
)