from django.shortcuts import render
from AboutUs.models import Teacher

# Create your views here.
def teachers_info(request):
    teach = Teacher.object.all()
    return render(request, 'teachers.html', {'thr': teach})
