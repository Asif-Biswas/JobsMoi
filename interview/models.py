import uuid
from django.conf import settings
from django.db import models
# Create your models here.
from homePage.models import TimeStampMixin


class Interview(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    text = models.TextField()
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def comments(self):
        return InterviewComment.objects.filter(interview=self)


class InterviewComment(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text
