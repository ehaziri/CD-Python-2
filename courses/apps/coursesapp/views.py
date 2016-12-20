from django.shortcuts import render,redirect
from models import Course, Description, Comment
# Create your views here.
def index(request):
    courses = Course.objects.all()
    context={'courses': courses }
    return render(request, 'coursesapp/index.html', context)

def create(request):
    description=Description.objects.create(description=request.POST['description'])
    course=Course.objects.create(name=request.POST['name'],
    description=description)

    return redirect('/')

def destroy(request, id):
    to_delete=Course.objects.get(id=id)
    context={'course_to_delete': to_delete}
    if request.method=='GET':
        return render(request, 'coursesapp/confirmation.html', context)
    to_delete.delete()
    return redirect('/')

def show_comments(request, id):
    course=Course.objects.get(id=id)
    comments=Comment.objects.filter(course=course)
    context={'comments': comments}
    return render(request, 'coursesapp/comments.html', context)

def add_comment(request, id):
    course=Course.objects.get(id=id)
    comment=Comment.objects.create(comment=request.POST['comment'], course=course)
    return redirect('/')
