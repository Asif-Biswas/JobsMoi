from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Message, Conversation
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from auths.models import Users as User
from django.contrib import messages as django_messages

# Create your views here.

def messages(request, active_conversation=None):
    if not request.user.is_authenticated:
        message = 'You need to login to view messages.'
        django_messages.add_message(request, django_messages.WARNING, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    conversations = Conversation.objects.filter(user_one=request.user) | Conversation.objects.filter(user_two=request.user)
    # order by last message date
    conversations = conversations.order_by('-updated')

    if active_conversation:
        active_conversation = Conversation.objects.get(id=active_conversation)
    else:
        active_conversation = conversations[0] if conversations else []
    
    context = {
        'conversations': conversations,
        'active_conversation': active_conversation
    }
    return render(request, 'messages.html', context)

@login_required(login_url='/')
def send_message(request, user_id):
    if request.method == 'POST':
        message = request.POST['message']
        receiver = User.objects.get(id=user_id)
        sender = request.user
        conversation = Conversation.objects.filter(
            Q(user_one=sender, user_two=receiver) | Q(user_one=receiver, user_two=sender))
        if conversation:
            conversation = conversation[0]
        else:
            conversation = Conversation.objects.create(user_one=sender, user_two=receiver)
        message = Message.objects.create(sender=sender, receiver=receiver, text=message)
        conversation.messages.add(message)
        conversation.save()
        return redirect('messages')
    else:
        return redirect('messages')


def start_conversation(request, user_id):
    if not request.user.is_authenticated:
        message = 'You need to login to view messages.'
        django_messages.add_message(request, django_messages.WARNING, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    receiver = User.objects.get(id=user_id)
    sender = request.user
    conversation = Conversation.objects.filter(
        Q(user_one=sender, user_two=receiver) | Q(user_one=receiver, user_two=sender))
    if not conversation:
        Conversation.objects.create(user_one=sender, user_two=receiver)
        
    return redirect('messages')

