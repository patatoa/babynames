# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NameInfo'
        db.create_table(u'babynames_app_nameinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.FirstName'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.Country'], null=True)),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['babynames_app.Gender'])),
            ('meaning', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'babynames_app', ['NameInfo'])

        # Adding field 'FullName.rank'
        db.add_column(u'babynames_app_fullname', 'rank',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FullName.pros'
        db.add_column(u'babynames_app_fullname', 'pros',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'FullName.cons'
        db.add_column(u'babynames_app_fullname', 'cons',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Deleting field 'FirstName.firstName'
        db.delete_column(u'babynames_app_firstname', 'firstName')

        # Deleting field 'FirstName.country'
        db.delete_column(u'babynames_app_firstname', 'country_id')

        # Deleting field 'FirstName.rank'
        db.delete_column(u'babynames_app_firstname', 'rank')

        # Deleting field 'FirstName.meaning'
        db.delete_column(u'babynames_app_firstname', 'meaning')

        # Deleting field 'FirstName.gender'
        db.delete_column(u'babynames_app_firstname', 'gender_id')

        # Adding field 'FirstName.name'
        db.add_column(u'babynames_app_firstname', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=25),
                      keep_default=False)

        # Adding M2M table for field nicknames on 'FirstName'
        m2m_table_name = db.shorten_name(u'babynames_app_firstname_nicknames')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_firstname', models.ForeignKey(orm[u'babynames_app.firstname'], null=False)),
            ('to_firstname', models.ForeignKey(orm[u'babynames_app.firstname'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_firstname_id', 'to_firstname_id'])


    def backwards(self, orm):
        # Deleting model 'NameInfo'
        db.delete_table(u'babynames_app_nameinfo')

        # Deleting field 'FullName.rank'
        db.delete_column(u'babynames_app_fullname', 'rank')

        # Deleting field 'FullName.pros'
        db.delete_column(u'babynames_app_fullname', 'pros')

        # Deleting field 'FullName.cons'
        db.delete_column(u'babynames_app_fullname', 'cons')

        # Adding field 'FirstName.firstName'
        db.add_column(u'babynames_app_firstname', 'firstName',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=20),
                      keep_default=False)

        # Adding field 'FirstName.country'
        db.add_column(u'babynames_app_firstname', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['babynames_app.Country']),
                      keep_default=False)

        # Adding field 'FirstName.rank'
        db.add_column(u'babynames_app_firstname', 'rank',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FirstName.meaning'
        db.add_column(u'babynames_app_firstname', 'meaning',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'FirstName.gender'
        db.add_column(u'babynames_app_firstname', 'gender',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['babynames_app.Gender']),
                      keep_default=False)

        # Deleting field 'FirstName.name'
        db.delete_column(u'babynames_app_firstname', 'name')

        # Removing M2M table for field nicknames on 'FirstName'
        db.delete_table(db.shorten_name(u'babynames_app_firstname_nicknames'))


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
            'nicknames': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['babynames_app.FirstName']", 'symmetrical': 'False'})
        },
        u'babynames_app.fullname': {
            'Meta': {'object_name': 'FullName'},
            'cons': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'first': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['babynames_app.FirstName']"}),
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