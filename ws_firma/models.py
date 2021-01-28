from django.db import models

class Documento(models.Model):
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # empresa_id = models.IntegerField(default=None, blank=True, null=True)
    # clave_acceso = models.TextField(default=None, blank=True, null=True)
    #autorizacion = models.IntegerField(blank=True, null=True)
    # documento_tipo = models.TextField(default=None, blank=True, null=True)
    documento = models.TextField(default=None, blank=True, null=True)
    documento_firmado = models.TextField(default=None, blank=True, null=True)
    
    class Meta:
        ordering = ['fecha_creacion']