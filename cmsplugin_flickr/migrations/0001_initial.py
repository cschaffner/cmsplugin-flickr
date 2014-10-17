# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, connection


class Migration(SchemaMigration):

    def forwards(self, orm):
        table_names = connection.introspection.table_names()
        if 'cmsplugin_flickr' in table_names:
            db.rename_table('cmsplugin_flickr', 'cmsplugin_flickr_flickr')
        elif 'flickr_flickr' in table_names:
            db.rename_table('flickr_flickr', 'cmsplugin_flickr_flickr')
        else:
            # Adding model 'Flickr'
            db.create_table(u'cmsplugin_flickr_flickr', (
                (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
                ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
                ('show_title', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
                ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
                ('group_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
                ('tags', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
                ('tags_match', self.gf('django.db.models.fields.CharField')(default='any', max_length=3)),
                ('size', self.gf('django.db.models.fields.CharField')(default='s', max_length=1)),
                ('order', self.gf('django.db.models.fields.CharField')(default='relevance', max_length=50)),
            ))
            db.send_create_signal(u'cmsplugin_flickr', ['Flickr'])


    def backwards(self, orm):
        # Deleting model 'Flickr'
        db.delete_table(u'cmsplugin_flickr_flickr')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_flickr.flickr': {
            'Meta': {'object_name': 'Flickr', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'default': "'relevance'", 'max_length': '50'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'s'", 'max_length': '1'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tags_match': ('django.db.models.fields.CharField', [], {'default': "'any'", 'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_flickr']