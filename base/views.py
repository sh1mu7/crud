from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from base.forms import StudentForm
from base.models import Student


# Create your views here.


def add_show(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    information = Student.objects.all()
    context = {
        'information': information
    }
    return render(request, 'add_show.html', context)


def delete(request, id):
    if request.method == 'POST':
        sid = Student.objects.get(pk=id)
        sid.delete()
        return HttpResponseRedirect('/')


def update(request, id):
    sid = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, instance=sid)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, 'update_delete.html', context)
