from django.shortcuts import render
from .models import Studentnew

def student_view(request):
    if request.method == 'POST':
        usn = request.POST.get('usn')
        name = request.POST.get('name')
        cie_marks = request.POST.get('cie_marks')

        Studentnew.objects.create(
            usn =usn,
            name=name,
            cie_marks=cie_marks
        )

    students =Studentnew.objects.filter(cie_marks__lt=20)

    return render(request,'index.html',{'students':students})

