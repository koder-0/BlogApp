from django.shortcuts import render

# Create your views here.
posts = [
            {
                'author' : 'koder-0',
                'title' : 'Post 0',
                'content' : 'dummy post 0',
                'date_published' : 'July 14, 2023'
            },
            {
                'author' : 'koder-1',
                'title' : 'Post 1',
                'content' : 'dummy post 1',
                'date_published' : 'July 14, 2023'
            }
        ]
def home(request):
    context = {
                'posts' : posts,
                'title' : 'Home'
              }
    return render(request, 'BlogApp/home.html', context)

def about(request):
    context = {
                'title' : 'About'
              }
    return render(request, 'BlogApp/about.html', context)
