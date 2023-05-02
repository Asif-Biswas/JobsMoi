from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Interview, InterviewComment
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def interview(request):
    interviews = Interview.objects.all().order_by('-created_at')
    paginator = Paginator(interviews, 5)
    page_number = request.GET.get('page')
    interviews = paginator.get_page(page_number)
    return render(request, 'interview.html', {'interviews': interviews})


def createInterview(request):
    # check if user is logged in
    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, f'You need to login to create a interview.')
        return redirect('interview')
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        company = request.POST.get('company')
        role = request.POST.get('role')
        interview = Interview(title=title, text=description, company=company, role=role, author=request.user)
        interview.save()
        messages.add_message(request, messages.SUCCESS, f'Your Interview has been created successfully.')

    return redirect('interview')


def interviewDetails(request, interview_id):
    interview = Interview.objects.get(id=interview_id)
    return render(request, 'interviewDetails.html', {'interview': interview})


def addComment(request, interview_id):
    # check if user is logged in
    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, f'You need to login to add a comment.')
        return redirect('interview')
    
    if request.method == "POST":
        text = request.POST.get('comment')
        interview = Interview.objects.get(id=interview_id)
        comment = InterviewComment(text=text, interview=interview, author=request.user)
        comment.save()
        messages.add_message(request, messages.SUCCESS, f'Your Comment has been added successfully.')

    return redirect('interview_details', interview_id=interview_id)

def deleteInterview(request, interview_id):
    interview = Interview.objects.get(id=interview_id)
    if interview.author != request.user:
        messages.add_message(request, messages.WARNING, f'You are not authorized to delete this interview.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    interview.delete()
    messages.add_message(request, messages.SUCCESS, f'Your Interview has been deleted successfully.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editInterview(request, interview_id):
    interview = Interview.objects.get(id=interview_id)
    if interview.author != request.user:
        messages.add_message(request, messages.WARNING, f'You are not authorized to edit this interview.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        company = request.POST.get('company')
        role = request.POST.get('role')
        interview.title = title
        interview.text = description
        interview.company = company
        interview.role = role
        interview.save()
        messages.add_message(request, messages.SUCCESS, f'Your Interview has been edited successfully.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteComment(request, comment_id):
    comment = InterviewComment.objects.get(id=comment_id)
    if comment.author != request.user:
        messages.add_message(request, messages.WARNING, f'You are not authorized to delete this comment.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    comment.delete()
    messages.add_message(request, messages.SUCCESS, f'Your Comment has been deleted successfully.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editComment(request, comment_id):
    comment = InterviewComment.objects.get(id=comment_id)
    if comment.author != request.user:
        messages.add_message(request, messages.WARNING, f'You are not authorized to edit this comment.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        text = request.POST.get('comment')
        comment.text = text
        comment.save()
        messages.add_message(request, messages.SUCCESS, f'Your Comment has been edited successfully.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

