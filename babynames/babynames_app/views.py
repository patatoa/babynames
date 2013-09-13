from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from babynames_app.models import FullName
from django.shortcuts import redirect


def main(request):
    names = FullName.objects.order_by('-rank')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))


def like(request, name_id):
    if name_id:
        name = FullName.objects.get(id=name_id)
        name.rank += 1
        name.save()

    return redirect('/')

def vote_down(request, name_id):
    if name_id:
        name = FullName.objects.get(id=name_id)
        name.rank -= 1
        name.save()

    return redirect('/')
