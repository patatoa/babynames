# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LastName'
        db.create_table(u'babynames_app_lastname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'babynames_app', ['LastName'])

        # Adding model 'FirstName'
        db.create_table(u'babynames_app_firstname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.Country'])),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.Gender'])),
            ('meaning', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'babynames_app', ['FirstName'])

        # Adding model 'Country'
        db.create_table(u'babynames_app_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countryName', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal(u'babynames_app', ['Country'])

        # Adding model 'FullName'
        db.create_table(u'babynames_app_fullname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.FirstName'])),
            ('last', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.LastName'])),
        ))
        db.send_create_signal(u'babynames_app', ['FullName'])

        # Adding model 'Gender'
        db.create_table(u'babynames_app_gender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genderAccronym', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('genderLabel', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal(u'babynames_app', ['Gender'])


    def backwards(self, orm):
        # Deleting model 'LastName'
        db.delete_table(u'babynames_app_lastname')

        # Deleting model 'FirstName'
        db.delete_table(u'babynames_app_firstname')

        # Deleting model 'Country'
        db.delete_table(u'babynames_app_country')

        # Deleting model 'FullName'
        db.delete_table(u'babynames_app_fullname')

        # Deleting model 'Gender'
        db.delete_table(u'babynames_app_gender')


    models = {
        u'babynames_app.country': {
            'Meta': {'object_name': 'Country'},
            'countryName': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'babynames_app.firstname': {
            'Meta': {'object_name': 'FirstName'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.Country']"}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'babynames_app.fullname': {
            'Meta': {'object_name': 'FullName'},
            'first': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.FirstName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.LastName']"})
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
        }
    }

    complete_apps = ['babynames_app']