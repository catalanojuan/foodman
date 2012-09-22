
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from foodman.apps.core.choosing import choose_foodman
from foodman.apps.core.forms import ChooseForm


@login_required
def landing(request):
    if request.method == 'GET':
        return render_to_response('choose.html',{
                    'form': ChooseForm(),
                },context_instance=RequestContext(request))

    return HttpResponse('Only GET method supported.', status=400)

@login_required
def choose(request):
    if request.method == 'GET':
        form = ChooseForm(request.GET)
        if not form.is_valid():
            return render_to_response('choose.html',{
                'form': ChooseForm(),
                'message': 'Invalid amount parameter.', 
                }, context_instance=RequestContext(request))

        choices_num = form.cleaned_data.get('num_choices', 2)

        choices = choose_foodman(int(choices_num))

        return render_to_response('choose.html',{
                    'choices': choices,
                },context_instance=RequestContext(request))

    return HttpResponse('Only GET method supported.', status=400)
