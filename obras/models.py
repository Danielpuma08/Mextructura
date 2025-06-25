from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

class Estado(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Ciudad(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Rol(models.Model):
    nombre = models.CharField(max_length=40)

class Persona(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

class EstadoTarea(models.Model):
    nombre = models.CharField(max_length=40)

class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=50)

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=30)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    rfc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=40)

class EstadoObra(models.Model):
    nombre = models.CharField(max_length=20)

class Obra(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='obras_supervisadas')
    estado_obra = models.ForeignKey(EstadoObra, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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

class EstadoFase(models.Model):
    nombre = models.CharField(max_length=20)

class Fase(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    estado_fase = models.ForeignKey(EstadoFase, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    porcentaje_avance = models.IntegerField()

class Tarea(models.Model):
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    estado_tarea = models.ForeignKey(EstadoTarea, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    porcentaje_avance = models.IntegerField()

class Evidencia(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    foto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120)
    fecha = models.DateTimeField()

class Material(models.Model):
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=60)
    fecha_registro = models.DateTimeField()
    activo = models.BooleanField(default=True)

class MaterialObra(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    fecha_uso = models.DateTimeField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)

class DetalleCompra(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    detalle_compra = models.ForeignKey(DetalleCompra, on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.FloatField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)

class Funcion(models.Model):
    nombre = models.CharField(max_length=30)

class EmpleadoObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
