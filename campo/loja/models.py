from django.db import models
class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

# Create your models here.
