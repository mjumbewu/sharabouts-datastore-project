from django.http import HttpResponseBadRequest
from django.utils.timezone import datetime, now
from djangorestframework import views, mixins
from djangorestframework.response import ErrorResponse
from djangorestframework.status import HTTP_400_BAD_REQUEST
from .forms import ActivityStreamForm
from .models import Point, Comment, Vote
from .resources import PointResource, CommentResource, VoteResource


class ActivityStreamView(views.View):
    def get(self, request, project_slug=None, *args, **kwargs):

        # Retrieve and validate any query parameters.
        form = ActivityStreamForm(request.GET)
        if not form.is_valid():
            raise ErrorResponse(HTTP_400_BAD_REQUEST, form.errors)

        before = form.cleaned_data.get('before', now())
        count = form.cleaned_data.get('count', 50)

        # Build the queries for the activities, including filtering by project
        # it it's specified.
        comments = Comment.objects.filter(created_at__lt=before).order_by('-created_at')
        points = Point.objects.filter(created_at__lt=before).order_by('-created_at')
        votes = Vote.objects.filter(created_at__lt=before).order_by('-created_at')

        if project_slug:
            comments.filter_by(commentable__project__slug=project_slug)
            points.filter_by(project__slug=project_slug)
            votes.filter_by(supportable__project__slug=project_slug)

        # Because we don't know exactly how many of each we need, just get the
        # same, maximum amount of each.
        comments = comments[:count]
        points = points[:count]
        votes = votes[:count]

        # Sort all the activity into one list.
        activity = sorted((
            CommentResource.serialize(comments) +
            PointResource.serialize(points) +
            VoteResource.serialize(votes)
        ), lambda elem: elem['created_at'])

        # Return no more than the requested number of results.
        return activity[count::-1]


class ReadInstanceModelView(mixins.InstanceMixin, mixins.ReadModelMixin, views.ModelView):
    """
    A view which provides read-only access to a model instance.
    """
    _suffix = 'Instance'
