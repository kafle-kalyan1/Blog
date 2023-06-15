from django.shortcuts import get_object_or_404, render, redirect
from Blog.models import Blog, Comment, BlogView, UpDown
from django.db.models import Q
from django.contrib import messages

from django.http import HttpResponseRedirect, JsonResponse


# Create your views here.
def blog(request):
    AllBlogs = Blog.objects.all()

    return render(request, 'Blog/blog.html', {"AllBlogs": AllBlogs})


def blogPost(request, id):
    try:
        blog = Blog.objects.get(id=id)
        blog_view, _ = BlogView.objects.update_or_create(blog=blog)
        blog_view.views += 1
        blog_view.save()

        comments = Comment.objects.filter(blog_id=id).order_by('-datetime')
        updowns = []

        if request.user.is_authenticated:
            for comment in comments:
                upvoted = UpDown.objects.filter(user=request.user, comment=comment, upvotes=True).exists()
                downvoted = UpDown.objects.filter(user=request.user, comment=comment, downvotes=True).exists()
                updowns.append({'comment_id': comment.id, 'upvoted': upvoted, 'downvoted': downvoted})
                print(updowns, downvoted, upvoted)
        para = {"blog": blog, "comments": comments, "views": blog_view.views, "updowns": updowns}
    except Blog.DoesNotExist:
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
        messages.success(request, 'Comment Added Sucesfully!')
    
        Comment.objects.create(blog=blog, user=user, content=comment_content)

    return redirect('blogPost', id=blog_id)

def upvote_comment(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            comment_id = request.POST.get('comment_id')
            comment = Comment.objects.get(id=comment_id)

            # Check if the user has already upvoted the comment
            upvote_exists = UpDown.objects.filter(user=request.user, comment=comment, upvotes=True).exists()

            if not upvote_exists:
                # Update the comment's upvotes count
                comment.upvotes += 1
                comment.save()

                # Create or update the user's upvote record
                updown, created = UpDown.objects.get_or_create(comment=comment, user=request.user)
                updown.upvotes = True
                updown.save()

            return JsonResponse({'upvotes': comment.upvotes})
        else:
            return HttpResponseRedirect('/login/')


def downvote_comment(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            comment_id = request.POST.get('comment_id')
            comment = Comment.objects.get(id=comment_id)

            # Check if the user has already downvoted the comment
            downvote_exists = UpDown.objects.filter(user=request.user, comment=comment, upvotes=False).exists()

            if not downvote_exists:
                # Update the comment's downvotes count
                comment.downvotes += 1
                comment.save()

                # Create or update the user's downvote record
                updown, created = UpDown.objects.get_or_create(comment=comment, user=request.user)
                updown.upvotes = False
                updown.save()

            return JsonResponse({'downvotes': comment.downvotes})
        else:
            return HttpResponseRedirect('/login/')