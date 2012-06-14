from django.conf.urls import patterns, include, url
from djangorestframework.views import ListModelView, InstanceModelView
from .resources import CommentResource, ContributorResource, PointResource, RegionResource, VoteResource, ProjectResource
from .views import ActivityStreamView, ReadInstanceModelView

urlpatterns = patterns('shareabouts',
    url(r'^(?:(?P<commentable__project__slug>[^/]*)/)?comments/$', ListModelView.as_view(resource=CommentResource)),
    url(r'^(?:(?P<commentable__project__slug>[^/]*)/)?comments/(?P<pk>.*)', ReadInstanceModelView.as_view(resource=CommentResource)),

    # This one's tricky; a contributor doesn't have a project.
    url(r'^contributors/$', ListModelView.as_view(resource=ContributorResource)),
    url(r'^contributors/(?P<pk>.*)', ReadInstanceModelView.as_view(resource=ContributorResource)),

    url(r'^projects/$', ListModelView.as_view(resource=ProjectResource)),
    url(r'^projects/(?P<pk>.*)', ReadInstanceModelView.as_view(resource=ProjectResource)),

    url(r'^(?:(?P<project__slug>[^/]*)/)?points/$', ListModelView.as_view(resource=PointResource)),
    url(r'^(?:(?P<project__slug>[^/]*)/)?points/(?P<pk>.*)', ReadInstanceModelView.as_view(resource=PointResource)),

    url(r'^(?:(?P<project__slug>[^/]*)/)?regions/$', ListModelView.as_view(resource=RegionResource)),
    url(r'^(?:(?P<project__slug>[^/]*)/)?regions/(?P<pk>.*)', ReadInstanceModelView.as_view(resource=RegionResource)),

    url(r'^(?:(?P<supportable__project__slug>[^/]*)/)?votes/$', ListModelView.as_view(resource=VoteResource)),
    url(r'^(?:(?P<supportable__project__slug>[^/]*)/)?votes/(?P<pk>.*)', ReadInstanceModelView.as_view(resource=VoteResource)),

    url(r'^(?:(?P<project_slug>[^/]*)/)?activity$', ActivityStreamView.as_view()),
)
