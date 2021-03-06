# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Facebook_Status_Attachment.caption'
        db.alter_column(u'facebook_feeds_facebook_status_attachment', 'caption', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Facebook_Status_Attachment.name'
        db.alter_column(u'facebook_feeds_facebook_status_attachment', 'name', self.gf('django.db.models.fields.TextField')(null=True))
        # Adding unique constraint on 'Facebook_Status_Attachment_Media', fields ['attachment', 'link']
        db.create_unique(u'facebook_feeds_facebook_status_attachment_media', ['attachment_id', 'link'])


    def backwards(self, orm):
        # Removing unique constraint on 'Facebook_Status_Attachment_Media', fields ['attachment', 'link']
        db.delete_unique(u'facebook_feeds_facebook_status_attachment_media', ['attachment_id', 'link'])


        # Changing field 'Facebook_Status_Attachment.caption'
        db.alter_column(u'facebook_feeds_facebook_status_attachment', 'caption', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Facebook_Status_Attachment.name'
        db.alter_column(u'facebook_feeds_facebook_status_attachment', 'name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'facebook_feeds.facebook_feed': {
            'Meta': {'ordering': "['feed_type']", 'object_name': 'Facebook_Feed', '_ormbases': [u'facebook_feeds.Facebook_Feed_Generic']},
            'about': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'birthday': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'facebook_feed_generic_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['facebook_feeds.Facebook_Feed_Generic']", 'unique': 'True', 'primary_key': 'True'}),
            'feed_type': ('django.db.models.fields.CharField', [], {'default': "'PP'", 'max_length': '2'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'page_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'null': 'True'}),
            'pic_large': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'null': 'True'}),
            'pic_square': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'null': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True'}),
            'vendor_id': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'null': 'True'})
        },
        u'facebook_feeds.facebook_feed_generic': {
            'Meta': {'object_name': 'Facebook_Feed_Generic'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'facebook_feeds.facebook_status': {
            'Meta': {'object_name': 'Facebook_Status'},
            'comment_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facebook_feeds.Facebook_Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'share_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'status_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'facebook_feeds.facebook_status_attachment': {
            'Meta': {'object_name': 'Facebook_Status_Attachment'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'facebook_object_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'attachment'", 'unique': 'True', 'to': u"orm['facebook_feeds.Facebook_Status']"})
        },
        u'facebook_feeds.facebook_status_attachment_media': {
            'Meta': {'unique_together': "(('attachment', 'link'),)", 'object_name': 'Facebook_Status_Attachment_Media'},
            'alt': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'attachment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': u"orm['facebook_feeds.Facebook_Status_Attachment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True'}),
            'owner_id': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'})
        },
        u'facebook_feeds.feed_popularity': {
            'Meta': {'ordering': "['-date_of_creation']", 'object_name': 'Feed_Popularity'},
            'date_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 22, 0, 0)'}),
            'fan_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facebook_feeds.Facebook_Feed']"}),
            'followers_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'friends_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'talking_about_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'facebook_feeds.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_main_display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'statuses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['facebook_feeds.Facebook_Status']"})
        },
        u'facebook_feeds.user_token': {
            'Meta': {'object_name': 'User_Token'},
            'date_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 22, 0, 0)'}),
            'date_of_expiration': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 6, 21, 0, 0)'}),
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tokens'", 'symmetrical': 'False', 'to': u"orm['facebook_feeds.Facebook_Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'user_id': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['facebook_feeds']