from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Places
import json
# Create your views here.


def home(request):
    if User.is_authenticated:
        events = Places.objects.all()
        param = {'events': events}
        for i in events:
            if request.user in i.like_by.all():
                i.like = True
            else:
                i.like = False
        return render(request, 'home.html', param)

    else:
        return HttpResponse("Page Not Found")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username} Accout Created Successfully')
            return redirect('/login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def event(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        data = request.POST['data']
        time = request.POST['time']
        location = request.POST['location']
        image = request.FILES.get('image')
        einput = Places(event_name=event_name, data=data,
                        time=time, location=location, image=image)
        einput.save()
        messages.success(request, 'Successfully Submitted')
    return render(request, 'event.html')


def like(request, pk):
    place = Places.objects.get(event_id=pk)
    if request.user in place.like_by.all():
        place.like_by.remove(request.user)
        place.save()
        response = json.dumps({"response": False})
        return HttpResponse(response)
    else:
        place.like_by.add(request.user)
        place.save()
        response = json.dumps({"response": True})
        return HttpResponse(response)
