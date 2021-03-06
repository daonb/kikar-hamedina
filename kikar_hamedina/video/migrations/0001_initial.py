# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'video_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('embed_link', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('image_link', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('small_image_link', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('source_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
            ('sticky', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hide', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_pk', self.gf('django.db.models.fields.TextField')()),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'video', ['Video'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'video_video')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'video.video': {
            'Meta': {'object_name': 'Video'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'embed_link': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'small_image_link': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['video']