from django.db import models
from django.contrib.auth.models import AbstractUser

class Paises(models.Model):
    cve_paises = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Estados(models.Model):
    cve_estados = models.AutoField(primary_key=True)
    cve_paises = models.ForeignKey(Paises, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class municipios(models.Model):
    cve_municipios = models.AutoField(primary_key=True)
    cve_estados = models.ForeignKey(Estados, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class ciudades(models.Model):
    cve_ciudades = models.AutoField(primary_key=True)
    cve_municipios = models.ForeignKey(municipios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class roles(models.Model):
    cve_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

class personas(AbstractUser):
    cve_personas = models.AutoField(primary_key=True)
    cve_rol = models.ForeignKey(roles, on_delete=models.CASCADE)
    ap_paterno = models.CharField(max_length=40)
    ap_materno = models.CharField(max_length=40)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
    
# class personas(AbstractUser):
#     cve_personas = models.AutoField(primary_key=True)
#     cve_rol = models.ForeignKey(roles, on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=40)
#     ap_paterno = models.CharField(max_length=40)
#     ap_materno = models.CharField(max_length=40)
#     email = models.CharField(max_length=40)
#     password = models.CharField(max_length=20)
#     direccion = models.CharField(max_length=80)
#     telefono = models.CharField(max_length=10)
#     activo = models.BooleanField(default=True)

class estados_tarea(models.Model):
    cve_estados_tarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

class tipos_material(models.Model):
    cve_tipos_material = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class unidades_medida(models.Model):
    cve_unidades_medida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Clientes(models.Model):
    cve_clientes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    ap_paterno = models.CharField(max_length=40)
    ap_materno = models.CharField(max_length=40)
    rfc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=40)

class estados_obra(models.Model):
    cve_estados_obra = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class obras(models.Model):
    cve_obras = models.AutoField(primary_key=True)
    cve_ciudades = models.ForeignKey(ciudades, on_delete=models.CASCADE)
    cve_supervisor = models.ForeignKey(personas, on_delete=models.CASCADE, related_name='supervisor_obras')
    cve_estados_obra = models.ForeignKey(estados_obra, on_delete=models.CASCADE)
    cve_clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    presupuesto = models.FloatField()
    porcentaje_avance = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()

class Estados_fase(models.Model):
    cve_estado_fase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class fases(models.Model):
    cve_fases = models.AutoField(primary_key=True)
    cve_obras = models.ForeignKey(obras, on_delete=models.CASCADE)
    cve_estado_fase = models.ForeignKey(Estados_fase, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    porcentaje_avance = models.IntegerField()

class tareas(models.Model):
    cve_tareas = models.AutoField(primary_key=True)
    cve_fases = models.ForeignKey(fases, on_delete=models.CASCADE)
    cve_estados_tarea = models.ForeignKey(estados_tarea, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    porcentaje_avance = models.IntegerField()

class evidencias(models.Model):
    cve_evidencias = models.AutoField(primary_key=True)
    cve_tareas = models.ForeignKey(tareas, on_delete=models.CASCADE)
    foto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120)
    fecha = models.DateTimeField()

class materiales(models.Model):
    cve_materiales = models.AutoField(primary_key=True)
    cve_tipos_material = models.ForeignKey(tipos_material, on_delete=models.CASCADE)
    cve_unidades_medida = models.ForeignKey(unidades_medida, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=60)
    fecha_registro = models.DateTimeField()
    activo = models.BooleanField(default=True)

class materiales_obras(models.Model):
    cve_materiales_obras = models.AutoField(primary_key=True)
    cve_materiales = models.ForeignKey(materiales, on_delete=models.CASCADE)
    cve_obras = models.ForeignKey(obras, on_delete=models.CASCADE)
    cve_unidades_medida = models.ForeignKey(unidades_medida, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    fecha_uso = models.DateTimeField()

class provedores(models.Model):
    cve_provedores = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

class detalles_compras(models.Model):
    cve_detalles_compras = models.AutoField(primary_key=True)
    cve_materiales = models.ForeignKey(materiales, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()

class compras(models.Model):
    cve_compras = models.AutoField(primary_key=True)
    cve_provedores = models.ForeignKey(provedores, on_delete=models.CASCADE)
    cve_detalles_comprad = models.ForeignKey(detalles_compras, on_delete=models.CASCADE)
    cve_obras = models.ForeignKey(obras, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.FloatField()

class empleados(models.Model):
    cve_empleados = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    ap_paterno = models.CharField(max_length=40)
    ap_materno = models.CharField(max_length=40)

class funciones(models.Model):
    cve_funciones = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

class empleados_obras(models.Model):
    cve_obras = models.ForeignKey(obras, on_delete=models.CASCADE)
    cve_empleados = models.ForeignKey(empleados, on_delete=models.CASCADE)
    cve_funciones = models.ForeignKey(funciones, on_delete=models.CASCADE)

class habilidades_funciones(models.Model):
    cve_funciones = models.ForeignKey(funciones, on_delete=models.CASCADE)
    cve_empleados = models.ForeignKey(empleados, on_delete=models.CASCADE)
