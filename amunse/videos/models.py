 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField

# Regla para que funcionen las migraciones de south con los campos de django-tagging
from south.modelsinspector import add_introspection_rules
add_introspection_rules = ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"]) 

class Video(models.Model):
    '''Modelo que representa el tipo de contenido para Videos en este caso solo para funcionar con youtube'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    fecha = models.DateField('Fecha',blank = False, null = False)
    video = models.URLField('Url del Video',verify_exists=True,blank = False, null = False)
    descripcion = models.TextField('Descripción',blank = True, null = True)
    tags =  TagAutocompleteField()

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
    
    def save(self, force_insert=False, force_update=False):
        n = Video.objects.all().count()
        self.slug = str(n) + '-' + slugify(self.titulo)
        super(Video, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)  