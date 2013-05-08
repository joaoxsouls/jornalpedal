# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Edition'
        db.create_table('editions_edition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('highlight', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('editions', ['Edition'])


    def backwards(self, orm):
        # Deleting model 'Edition'
        db.delete_table('editions_edition')


    models = {
        'editions.edition': {
            'Meta': {'object_name': 'Edition'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'highlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['editions']