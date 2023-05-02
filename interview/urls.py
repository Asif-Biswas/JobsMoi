from django.urls import path
from . import views

urlpatterns = [
    path('interview', views.interview, name="interview"),
    path('create-interview', views.createInterview, name="create_interview"),
    path('interview-details/<str:interview_id>', views.interviewDetails, name="interview_details"),
    path('add-interview-comment/<str:interview_id>', views.addComment, name="add_interview_comment"),
    path('delete-interview/<str:interview_id>', views.deleteInterview, name='delete_interview'),
    path('delete-interview-comment/<str:comment_id>', views.deleteComment, name='delete_interview_comment'),

]