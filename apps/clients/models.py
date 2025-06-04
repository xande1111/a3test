from django.db import models
from socialNetworks.models import SocialNetwork

# Create your models here.

class Client(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    client_socialnetwork = models.ManyToManyField(SocialNetwork, through='ClientSocialnetwork', blank=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name


class ClientSocialnetwork(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Redes Social'
        verbose_name_plural = 'Itens de Rede Social'
        ordering =['id']

    def __str__(self):
        return self.socialnetwork.name