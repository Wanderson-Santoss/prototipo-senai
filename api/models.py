from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length= 200);
    descricao = models.TextField();
    data_inicio = models.DateField();
    data_termino = models.DateField();
    finalizada = models.BooleanField(default=False);

    def __str__(self):
        return self.titulo