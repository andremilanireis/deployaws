from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

class Instrumento(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, null=True, blank=True, related_name='instrumentos')
    marca = models.CharField(max_length=100)
    
    TIPOS_DE_INSTRUMENTO = (
        (1, 'violao'),
        (2, 'piano'),
        (3, 'cajon')
    )
    tipo = models.PositiveSmallIntegerField(choices=TIPOS_DE_INSTRUMENTO)

    foto = models.ImageField(upload_to='instrumentos', blank=True, null=True)

    def __str__(self):
        if self.tipo == 1:
            return "Violão " + self.marca 
        elif self.tipo == 2:
            return "Piano " + self.marca
        elif self.tipo == 3:
            return "Cajon " + self.marca
