from django.db import models

class Usuario(models.Model):
    cpf = models.IntegerField(default=0)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(default='2000-01-01')

    def __str__(self):
        return self.name