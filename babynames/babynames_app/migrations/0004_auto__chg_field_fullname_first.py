# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FullName.first'
        db.alter_column(u'babynames_app_fullname', 'first_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.NameInfo']))

    def backwards(self, orm):

        # Changing field 'FullName.first'
        db.alter_column(u'babynames_app_fullname', 'first_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.FirstName']))

    models = {
        u'babynames_app.country': {
            'Meta': {'object_name': 'Country'},
            'countryName': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'babynames_app.firstname': {
            'Meta': {'object_name': 'FirstName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'nicknames': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['babynames_app.FirstName']", 'null': 'True', 'symmetrical': 'False'})
        },
        u'babynames_app.fullname': {
            'Meta': {'object_name': 'FullName'},
            'cons': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'first': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.NameInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.LastName']"}),
            'pros': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'babynames_app.gender': {
            'Meta': {'object_name': 'Gender'},
            'genderAccronym': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'genderLabel': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'babynames_app.lastname': {
            'Meta': {'object_name': 'LastName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'babynames_app.nameinfo': {
            'Meta': {'object_name': 'NameInfo'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.Country']", 'null': 'True'}),
            'firstName': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.FirstName']"}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['babynames_app']