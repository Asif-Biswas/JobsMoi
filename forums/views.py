from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Discussion, Comment
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def forums(request):
    discussions = Discussion.objects.all().order_by('-created_at')
    paginator = Paginator(discussions, 5)
    page_number = request.GET.get('page')
    discussions = paginator.get_page(page_number)
    return render(request, 'forums.html', {'discussions': discussions})


def createForum(request):
    # check if user is logged in
    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, f'You need to login to create a forum.')
        return redirect('forums')
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        discussion = Discussion(title=title, text=description, author=request.user)
        discussion.save()
        messages.add_message(request, messages.SUCCESS, f'Your Forum has been created successfully.')

    return redirect('forums')


def forumDetails(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    return render(request, 'forumDetails.html', {'discussion': discussion})


def addComment(request, discussion_id):
    # check if user is logged in
    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, f'You need to login to add a comment.')
        return redirect('forums')
    
    if request.method == "POST":
        text = request.POST.get('comment')
        discussion = Discussion.objects.get(id=discussion_id)
        comment = Comment(text=text, discussion=discussion, author=request.user)
        comment.save()
        messages.add_message(request, messages.SUCCESS, f'Your Comment has been added successfully.')

    return redirect('forum_details', discussion_id=discussion_id) 

def deleteForum(request, discussion_id):
    discussion = Discussion.objects.get(id=discussion_id)
    if discussion.author != request.user:
        messages.add_message(request, messages.WARNING, f'You are not authorized to delete this forum.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    discussion.delete()
    messages.add_message(request, messages.SUCCESS, f'Your Forum has been deleted successfully.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleteComment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.author != request.user:
        messages.add_message(request, messages.WARNING, f'You are not authorized to delete this comment.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    comment.delete()
    messages.add_message(request, messages.SUCCESS, f'Your Comment has been deleted successfully.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))