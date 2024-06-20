from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    dtl = 'django template language'
    Teachers = ['Ravi', 'Rajesh', 'Rahul', 'Rohit']
    page = {'what':'Blogs', 'dt': dtl, 'teachers': Teachers}
    return render (request, 'blogs/blogs.html', context=page)
