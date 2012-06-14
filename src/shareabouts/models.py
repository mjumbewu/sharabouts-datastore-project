from django.contrib.gis.db import models
from utils.models import SlugifiedModelMixin

class Project (SlugifiedModelMixin, models.Model):
    name = models.CharField(max_length=100)

class Contributor (models.Model):
    zip_code = models.CharField(max_length=5)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Point (models.Model):
    project = models.ForeignKey('shareabouts.Project')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    contributor = models.ForeignKey('shareabouts.Contributor', null=True, blank=True, related_name='points')
    contributor_name = models.CharField(max_length=100)
    support_count = models.IntegerField(default=0) # is this just for efficiency?

class Comment (models.Model):
    comment = models.TextField()
    commentable = models.ForeignKey('shareabouts.Point')  # This should be a generic foreign key.
    submitter = models.ForeignKey('shareabouts.Contributor', null=True, blank=True)
    display_submitter = models.CharField(max_length=100)  # The contributor's name
    created_at = models.DateTimeField(auto_now_add=True)

class Vote (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # There's a user column that's always null(?).
    profile = models.ForeignKey('shareabouts.Contributor')
    supportable = models.ForeignKey('shareabouts.Point')  # This should be a generic foreign key.

class Region (models.Model):
    project = models.ForeignKey('shareabouts.Project')
    # created_at
    # update_at
    # the_geom
    pass
