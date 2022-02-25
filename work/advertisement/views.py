from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import advrt
from .form import advrtForm
from django.http import HttpResponse


# Create your views here.

def adver (request):
    if request.method == 'POST':
        fm = advrtForm(request.POST)
        if fm.is_valid():
            fm.save()
        return redirect('web')

    else:
        fm = advrtForm()

    return render(request, "adver.html", {'form': fm, })


def web (request):
    stud = advrt.objects.all()

    return render(request, 'web.html', {'stu': stud})


# this is used for the deletion of
def delete (request, id):
    if request.method == 'POST':
        pi = advrt.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/web')


def update (request, id):
    if request.method == "POST":
        pi = advrt.objects.get(pk=id)
        fm = advrtForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('web')

    else:
        pi = advrt.objects.get(pk=id)
        fm = advrtForm(instance=pi)
    return render(request, "update_rec.html", {'form': fm })
from django.shortcuts import render

# Create your views here.
