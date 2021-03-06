# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Facebook_Feed.about'
        db.add_column(u'core_facebook_feed', 'about',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.birthday'
        db.add_column(u'core_facebook_feed', 'birthday',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.fan_count'
        db.add_column(u'core_facebook_feed', 'fan_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facebook_Feed.name'
        db.add_column(u'core_facebook_feed', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.page_url'
        db.add_column(u'core_facebook_feed', 'page_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.pic_large'
        db.add_column(u'core_facebook_feed', 'pic_large',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.pic_square'
        db.add_column(u'core_facebook_feed', 'pic_square',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.talking_about_count'
        db.add_column(u'core_facebook_feed', 'talking_about_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Facebook_Feed.username'
        db.add_column(u'core_facebook_feed', 'username',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True),
                      keep_default=False)

        # Adding field 'Facebook_Feed.website'
        db.add_column(u'core_facebook_feed', 'website',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Facebook_Feed.about'
        db.delete_column(u'core_facebook_feed', 'about')

        # Deleting field 'Facebook_Feed.birthday'
        db.delete_column(u'core_facebook_feed', 'birthday')

        # Deleting field 'Facebook_Feed.fan_count'
        db.delete_column(u'core_facebook_feed', 'fan_count')

        # Deleting field 'Facebook_Feed.name'
        db.delete_column(u'core_facebook_feed', 'name')

        # Deleting field 'Facebook_Feed.page_url'
        db.delete_column(u'core_facebook_feed', 'page_url')

        # Deleting field 'Facebook_Feed.pic_large'
        db.delete_column(u'core_facebook_feed', 'pic_large')

        # Deleting field 'Facebook_Feed.pic_square'
        db.delete_column(u'core_facebook_feed', 'pic_square')

        # Deleting field 'Facebook_Feed.talking_about_count'
        db.delete_column(u'core_facebook_feed', 'talking_about_count')

        # Deleting field 'Facebook_Feed.username'
        db.delete_column(u'core_facebook_feed', 'username')

        # Deleting field 'Facebook_Feed.website'
        db.delete_column(u'core_facebook_feed', 'website')


    models = {
        u'core.facebook_feed': {
            'Meta': {'object_name': 'Facebook_Feed'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'fan_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'page_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Person']"}),
            'pic_large': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic_square': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'talking_about_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'vendor_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'core.facebook_status': {
            'Meta': {'object_name': 'Facebook_Status'},
            'comment_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Facebook_Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'share_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'status_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'core.party': {
            'Meta': {'object_name': 'Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'core.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persons'", 'to': u"orm['core.Party']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'core.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'statuses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['core.Facebook_Status']"})
        }
    }

    complete_apps = ['core']