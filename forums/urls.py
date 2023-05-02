from django.urls import path, include

from . import views

urlpatterns = [
    path("forums", views.forums, name="forums"),
    path("create-forum", views.createForum, name="create_forum"),
    path("forum-details/<str:discussion_id>", views.forumDetails, name="forum_details"),
    path("add-comment/<str:discussion_id>", views.addComment, name="add_comment"),
    path('delete-forum/<str:discussion_id>', views.deleteForum, name='delete_forum'),
    path('delete-comment/<str:comment_id>', views.deleteComment, name='delete_comment'),
]