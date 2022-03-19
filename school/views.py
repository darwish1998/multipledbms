from django.shortcuts import render,redirect
from school.forms import SchoolForm
from .models import School
from .forms  import SchoolForm


# Create your views here.

def school(request):
    school = School.objects.all() 
    if request.method  == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SchoolForm()
    context = {
        'school': school,
        'form': form

    }
    return render(request, 'School/school.html',context)