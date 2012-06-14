from djangorestframework import resources
from .models import Comment, Contributor, Point, Vote, Region, Project

class CommentResource (resources.ModelResource):
    model = Comment

class ContributorResource (resources.ModelResource):
    model = Contributor

class PointResource (resources.ModelResource):
    model = Point

class VoteResource (resources.ModelResource):
    model = Vote

class RegionResource (resources.ModelResource):
    model = Region

class ProjectResource (resources.ModelResource):
    model = Project
