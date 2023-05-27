from django.shortcuts import render
from Blog.models import Blog
from django.db.models import Q

# Create your views here.
def blog(request):
    AllBlogs = Blog.objects.all()
    print(AllBlogs)
    return render(request, 'Blog/blog.html',{"AllBlogs":AllBlogs})

def blogPost(request, id):
    blogData2 = Blog.objects.filter(id=id)[0]
    para = {"blog":blogData2}
    print(blogData2)
    # for blog in blogData2:
    print(blogData2.description)

    return render(request, 'Blog/BlogPages.html',para)

def search_view(request):
    query = request.GET.get('query')
    results = Blog.objects.filter(
        Q(title__icontains=query.strip()) |
        Q(description__icontains=query.strip()) |
        Q(author__icontains=query.strip())
    )
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'Blog/search_results.html', context)