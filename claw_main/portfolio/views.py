from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def portfolio(request):
    """TODO: Docstring for portfolio.
    :returns: TODO

    """
    return render_to_response('portfolio.html',
                              context_instance=RequestContext(request)
                              )
