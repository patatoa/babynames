# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from babynames_app.models import FullName


def main(request):
    names = FullName.objects.order_by('rank')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))