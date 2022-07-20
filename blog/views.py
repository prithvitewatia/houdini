from django.shortcuts import render


def home(request):
    posts = [
        {
            "author": "CoreyMs",
            "title": "Title 1",
            "content": "Content of post1",
            "date_added": "January 1 2017"
        },
        {
            "author": "CoreyMs",
            "title": "Title 1",
            "content": "Content of post1",
            "date_added": "January 1 2017"
        },
        {
            "author": "CoreyMs",
            "title": "Title 1",
            "content": "Content of post1",
            "date_added": "January 1 2017"
        }
    ]
    context = {
        "pageTitle": "Blogs",
        "posts": posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
