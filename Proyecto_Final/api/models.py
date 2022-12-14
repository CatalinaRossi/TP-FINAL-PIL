from django.db import models

# Create your models here.
class Usuario(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)

class Nota(models.Model):

    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=200)
    autor=models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')