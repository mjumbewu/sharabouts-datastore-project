from django.contrib import admin
from .models import Project, Point, Comment, Contributor, Region, Vote

admin.site.register(Project)
admin.site.register(Point)
admin.site.register(Comment)
admin.site.register(Contributor)
admin.site.register(Region)
admin.site.register(Vote)
