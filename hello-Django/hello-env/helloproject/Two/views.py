import random

from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Student


def index(request):
    return HttpResponse('Two index')


def add_student(request):

    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(200)
    student.save()

    return HttpResponse('Add success %s 添加成功！' % student.s_name)



def get_students(request):

    students = Student.objects.all()

    for student in students:
        print(student.s_name)


    context = {
        "hobby": "play games",
        "students": students,
    }

    # return HttpResponse('students list')
    return render(request,'student_list.html',context=context)