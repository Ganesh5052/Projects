from django.shortcuts import render
from .models import StudentInfo

def homePage(request):
    if request.method == "GET":
        return render(request,'homePage.html')

    else:
        StudentInfo(
        first_name = request.POST.get('fname'),
        last_name = request.POST.get('lname'),
        email = request.POST.get('email'),
        mobile = request.POST.get('mobile'),
        location = request.POST.get('loc'),
        blood_group = request.POST.get('blood')
        ).save()
        return render(request,'homePage.html')
