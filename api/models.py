from django.db import models

# Create your models here.

class Genero(models.Model):
    idGenero = models.IntegerField(primary_key=True, db_column='idGenero')
    tipoGenero = models.CharField(max_length=100, db_column='tipoGenero')
    class Meta:
        db_table='Genero'
        
class Registro(models.Model):
    idRegistro = models.IntegerField(primary_key=True, db_column='idRegistro')
    usuario = models.CharField(max_length=100, db_column='usuario')
    correo = models.EmailField(db_column='correo')
    password = models.CharField(max_length=100, db_column='password')
    class Meta:
        db_table='Usuarios'

class Alumno(models.Model):
    idAlumnos = models.IntegerField(primary_key=True, db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100, db_column='nameAlumno')
    fk_genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='Alumnos'
        
class Alumno_has_Genero(models.Model):
    fk_Alumno = models.ForeignKey(Alumno,default=1,on_delete=models.CASCADE,db_column='fk_Alumno')
    fk_Genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_Genero')
    class Meta:
        db_table='alumno_has_genero'
        
# models.py

class Preguntas(models.Model):
    id_respuesta = models.AutoField(primary_key=True, db_column='id_respuesta')
    descripcion = models.CharField(max_length=255, db_column='P1')
    descripcion1 = models.CharField(max_length=255, db_column='P2')
    descripcion2 = models.CharField(max_length=255, db_column='P3')
    descripcion3 = models.CharField(max_length=255, db_column='P4')
    descripcion4 = models.CharField(max_length=255, db_column='P5')
    descripcion5 = models.CharField(max_length=255, db_column='P6')
    descripcion6 = models.CharField(max_length=255, db_column='P7')
    descripcion7 = models.CharField(max_length=255, db_column='P8')
    descripcion8 = models.CharField(max_length=255, db_column='P9')
    descripcion9 = models.CharField(max_length=255, db_column='P10')
    descripcion10 = models.CharField(max_length=255, db_column='P11')
    
    class Meta:
        db_table='Services'

