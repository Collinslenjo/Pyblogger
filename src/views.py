from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
	blogs = Blog.objects.all()[:10]
	context = {
		'name':'Blog Posts',
		'blogs':blogs
	}
	return render(request, 'index.html',context)

def details(request, id):
	blog = Blog.objects.get(id=id)
	context = {
	'blog':blog
	}
	return render(request, 'details.html',context)

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']

		blog = Blog(title=title,text=text)
		blog.save()
		return redirect('/blog')
	else:
	    return render(request, 'add.html')