from django.db import models
from datetime import date


#
class AppAdministracion_InsumosOficina(models.Model):  
  nro_articulo = models.IntegerField(blank=False, primary_key=True)
  nombre = models.CharField(max_length=50, blank=False, null=False)
  ubicacion = models.CharField(max_length=25, blank=False, null=False)
  stock = models.IntegerField(blank=False, null=False)
  descripcion = models.CharField(max_length=100, blank=False, null=False)

  def __str__(self):
    return self.nombre

  # def __unicode__(self):
  #   return 
  
  
#
class AppAdministracion_Vehiculos(models.Model):  
  patente = models.CharField(max_length=6, blank=False, primary_key=True)
  numero_chasis = models.CharField(max_length=17, blank=False, null=False, unique=True)
  marca = models.CharField(max_length=20, blank=False, null=False)
  modelo = models.CharField(max_length=10, blank=False, null=False)
  ultima_revision = models.DateField(blank=False, null=False, auto_now=True, verbose_name="Fecha (dd/mm/yyyy)")
  proxima_revision = models.DateField(blank=False, null=False, auto_now=True, verbose_name="Fecha (dd/mm/yyyy)")
  observaciones = models.CharField(max_length=200, blank=False, null=False)


#
class AppAdministracion_InsumosComputacionales(models.Model):  
  numero_insumo = models.IntegerField(blank=False, primary_key=True)
  nombre = models.CharField(max_length=50, blank=False, null=False)
  fecha_adquisicion = models.DateField(blank=False, null=False, auto_now=True, verbose_name="Fecha (dd/mm/yyyy)")
  marca = models.CharField(max_length=30, blank=False, null=False)
  stock = models.IntegerField(blank=False, null=False)
  descripcion = models.CharField(max_length=100, blank=False, null=False)
  
  
#
class AppAdministracion_Usuarios(models.Model):
  username = models.CharField(max_length=25, blank=False, primary_key=True)
  password = models.CharField(max_length=40, blank=False, null=False, unique=True)
  email = models.CharField(max_length=60, blank=False, null=False)
  nombre = models.CharField(max_length=60, blank=False, null=False)
  perfil = models.IntegerField(blank=False, null=False)
 
  
  
