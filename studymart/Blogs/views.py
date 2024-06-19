from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    dtl = 'django template language'
    page = {'what':'Blogs', 'dt': dtl}
    return render (request, 'blogs/blogs.html', context=page)
