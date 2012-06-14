# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('shareabouts_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('shareabouts', ['Project'])

        # Adding field 'Point.project'
        db.add_column('shareabouts_point', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['shareabouts.Project']),
                      keep_default=False)

        # Adding field 'Region.project'
        db.add_column('shareabouts_region', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['shareabouts.Project']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('shareabouts_project')

        # Deleting field 'Point.project'
        db.delete_column('shareabouts_point', 'project_id')

        # Deleting field 'Region.project'
        db.delete_column('shareabouts_region', 'project_id')


    models = {
        'shareabouts.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'commentable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shareabouts.Point']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_submitter': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shareabouts.Contributor']", 'null': 'True'})
        },
        'shareabouts.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'shareabouts.point': {
            'Meta': {'object_name': 'Point'},
            'contributor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'points'", 'null': 'True', 'to': "orm['shareabouts.Contributor']"}),
            'contributor_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shareabouts.Project']"}),
            'support_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shareabouts.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        'shareabouts.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shareabouts.Project']"})
        },
        'shareabouts.vote': {
            'Meta': {'object_name': 'Vote'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shareabouts.Contributor']"}),
            'supportable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shareabouts.Point']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['shareabouts']