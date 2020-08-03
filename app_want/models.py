from django.db import models
from django.contrib.auth.models import User


class bando(models.Model):
    nome=models.CharField("nome", max_length=30)
    imagem=models.FileField('jolly Roger',upload_to="jollyRoger")

    class Meta:
        verbose_name="bando"
    
    def __str__(self):
        return '{}'.format(self.nome)


class wanted(models.Model):
    Nome=models.CharField("nome", max_length=30)
    alcunha=models.CharField("alcunha", max_length=30)
    foto=models.FileField("imagem", upload_to='fotos')
    recompensa=models.FloatField('Berries')
    bando=models.ForeignKey(bando,on_delete=models.CASCADE)

    class Meta:
        verbose_name="wanted"
        verbose_name_plural="wanted's"
    
    def __str__(self):
        return '{} - {}'.format(self.Nome,self.alcunha)

class usuario(models.Model):
    nome=models.CharField('nome', max_length=15)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagem=models.FileField(upload_to='fotos', null=True)
    pontos=models.IntegerField('pontos')

    def __str__(self):
        return '{}'.format(self.user)


class texto(models.Model):
    choices=(['analise','1'],['publicado','2'])
    titulo=models.CharField("titulo", max_length=30)
    corpo=models.CharField("corpo", max_length=800)
    personagem=models.ForeignKey(wanted, on_delete=models.CASCADE)
    status=models.CharField(choices=choices, max_length=15)
    autor=models.ForeignKey(usuario,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.titulo,self.status)
    
