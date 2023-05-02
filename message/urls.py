from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.messages, name='messages'),
    path('messages/<int:active_conversation>', views.messages, name='messages'),
    path('send-message/<int:user_id>', views.send_message, name='send_message'),
    path('start-conversation/<int:user_id>', views.start_conversation, name='start_conversation'),
]
