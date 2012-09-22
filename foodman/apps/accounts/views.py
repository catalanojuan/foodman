
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def login_view(request):
    form = None
    message = None

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    message = 'Your account is not enabled'
            else:
                message = 'Username/password combination invalid.'
        else:
            message = 'Invalid login form.'
    else:
        form = AuthenticationForm()
        message = None

    return render_to_response('login.html', {
            'message': message,
            'form': form
        }, context_instance=RequestContext(request))
