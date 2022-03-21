from django.shortcuts import render, get_object_or_404
from .models import Blog

#yumi:
# Create your views here.
def all_blogs(request):
    #return render(request, 'blog/all_blogs.html')
    #blogs = Blog.objects.all()
    #recent one data, sorting and limiting
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})


# pass variable name
def detail(request,blog_id):
    #trying to find the object i.e. pk means primary key which is id, so if it doenst find it is will give us 404 page
    #name of class is 'Blog' which is defined in Model.py
    blog = get_object_or_404(Blog, pk = blog_id)
    #return render(request, 'blog/detail.html', {'id':blog_id})
    return render(request, 'blog/detail.html', {'blog':blog})
