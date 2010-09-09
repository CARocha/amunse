# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Archivo.adjunto4'
        db.delete_column('documentos_archivo', 'adjunto4')

        # Deleting field 'Archivo.adjunto3'
        db.delete_column('documentos_archivo', 'adjunto3')


    def backwards(self, orm):
        
        # Adding field 'Archivo.adjunto4'
        db.add_column('documentos_archivo', 'adjunto4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Archivo.adjunto3'
        db.add_column('documentos_archivo', 'adjunto3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)


    models = {
        'documentos.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'adjunto1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'}),
            'subcategoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.SubCategoriaDocumento']"})
        },
        'documentos.categoriadocumento': {
            'Meta': {'object_name': 'CategoriaDocumento'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'documentos.subcategoriadocumento': {
            'Meta': {'object_name': 'SubCategoriaDocumento'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.CategoriaDocumento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        }
    }

    complete_apps = ['documentos']
