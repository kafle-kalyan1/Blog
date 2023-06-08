from django.shortcuts import get_object_or_404, render, redirect
from Blog.models import Blog, Comment
from django.db.models import Q

from django.http import JsonResponse


# Create your views here.


def blog(request):
    AllBlogs = Blog.objects.all()

    return render(request, 'Blog/blog.html', {"AllBlogs": AllBlogs})


def blogPost(request, id):
    try:
        blogData2 = Blog.objects.filter(id=id)[0]
        comments = Comment.objects.filter(blog_id=id).order_by('-upvotes')
        para = {"blog": blogData2, "comments": comments}
    except:
        return redirect(blog)
    return render(request, 'Blog/BlogPages.html', para)


def search_view(request):
    query = request.GET.get('query')
    results = Blog.objects.filter(
        Q(title__icontains=query.strip()) |
        Q(description__icontains=query.strip())
    )
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'Blog/search_results.html', context)


def handleComment(request):
    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        comment_content = request.POST.get('comment')

        blog = get_object_or_404(Blog, id=blog_id)
        user = request.user

        Comment.objects.create(blog=blog, user=user, content=comment_content)

    return redirect('blogPost', id=blog_id)


from django.http import JsonResponse

def upvote_comment(request):
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.upvotes += 1
        comment.save()
        return JsonResponse({'upvotes': comment.upvotes})

def downvote_comment(request):
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.downvotes += 1
        comment.save()
        return JsonResponse({'downvotes': comment.downvotes})
