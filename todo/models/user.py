from django.contrib.auth.models import AbstractUser
from django.db import models

class UserEntity (AbstractUser):
    '''
        Esta é uma classe que representa um usuário neste sistema. Ao herdar da classe AbstractUser, recebe por padrão os seguintes atributos

        Atributos herdados:
            first_name 
            last_name
            username
            email
            is_staff
            is_active
            date_joined


        Atributos adicionados:
            birth__date (date field) : data de nascimento
            profile_picture (image field) : recbe uma imagem (byte array) e salva no caminho 'media/profiles/'

    '''
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to= 'media/profiles/',
        null=True, blank=True
    )

    #Redefinimos a forma que os valores do campo password é salvo no banco de dados
    def save(sellf, *args, **kwargs):
        #Defnimos o valor como "newPassword"
        sellf.password = "newPassword"
        #Realiza o save
        super().save(*args, **kwargs)