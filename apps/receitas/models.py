from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Define um modelo de objeto.

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_da_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_da_receita = models.ImageField(upload_to='foto/%d/%m/%Y', blank=True)
    def __str__(self):
        return self.nome_receita