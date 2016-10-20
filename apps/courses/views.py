from django.shortcuts import render, redirect
from .models import Course, Description, Comment

# Create your views here.
def index(request):

    context = {
      "courses" : Course.objects.all(),
      "descriptions" : Description.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    course = Course.objects.create(name=request.POST['name'])
    description = Description.objects.create(text = request.POST['desc'], course = course)
    print "JUST ADDED THESE THINGS", course.id, description.id
    return redirect('/')

def confirmDelete(request, id):
    course = Course.objects.get(id=id)
    context = {
      "doomed" : course
    }
    return render(request, 'courses/confirmdelete.html', context)

def delete(request):
    id = request.POST['id']
    course = Course.objects.get(id = id).delete()
    return redirect('/')

def viewcomments(request, id):
    course = Course.objects.get(id = id)
    comments = Comment.objects.filter(course = course)
    context = {
      'course' : course,
      'comments' : comments
    }
    return render(request, "courses/viewcomments.html", context)

def createcomment(request):
    courseid=request.POST['id']
    course = Course.objects.get(id = courseid)
    comment = Comment.objects.create(name = request.POST['name'], comment = request.POST['comment'], course = course)
    return redirect('/viewcomments/{}'.format(courseid))
