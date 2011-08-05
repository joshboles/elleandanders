from django.http import HttpResponseRedirect

class NoWWW:
    def process_request(self, request):
        if request.get_host() != "elleandandy.com":
            return HttpResponseRedirect("http://elleandandy.com%s" % request.get_full_path())
    
        if request.get_full_path() == "/favicon.ico":
            return HttpResponseRedirect("/static/img/favicon.ico")
