from django.shortcuts import render
'''
yumi: how to work on project inside of your db to show up on website inside the template,inside of our view.py we will grab the
Project object from db and then send them forward into the template which we can display at that point
'''
from .models import Project

#yumi:
# Create your views here.
def home(request):

    # grab all project objects from db
    projects = Project.objects.all()

    #return render(request,'portfolio/home.html')

    # pass the above project object into our template as dictionary and turn into a list
    return render(request,'portfolio/home.html', {'projects':projects})
