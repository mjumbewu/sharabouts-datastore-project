# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contributor'
        db.create_table('shareabouts_contributor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('shareabouts', ['Contributor'])

        # Adding model 'Point'
        db.create_table('shareabouts_point', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contributor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='points', null=True, to=orm['shareabouts.Contributor'])),
            ('contributor_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('support_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('shareabouts', ['Point'])

        # Adding model 'Comment'
        db.create_table('shareabouts_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('commentable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shareabouts.Point'])),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shareabouts.Contributor'], null=True)),
            ('display_submitter', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('shareabouts', ['Comment'])

        # Adding model 'Vote'
        db.create_table('shareabouts_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shareabouts.Contributor'])),
            ('supportable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shareabouts.Point'])),
        ))
        db.send_create_signal('shareabouts', ['Vote'])

        # Adding model 'Region'
        db.create_table('shareabouts_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('shareabouts', ['Region'])


    def backwards(self, orm):
        # Deleting model 'Contributor'
        db.delete_table('shareabouts_contributor')

        # Deleting model 'Point'
        db.delete_table('shareabouts_point')

        # Deleting model 'Comment'
        db.delete_table('shareabouts_comment')

        # Deleting model 'Vote'
        db.delete_table('shareabouts_vote')

        # Deleting model 'Region'
        db.delete_table('shareabouts_region')


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
            'support_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shareabouts.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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