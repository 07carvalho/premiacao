from django.db import models
from django.contrib.auth.models import User


class Edition(models.Model):

    '''
    Edição do premio. Ex: 2015, 2016, 2017
    '''

    class Meta:
        app_label = 'api'


    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return u'{0}'.format(self.name)


class Category(models.Model):

    '''
    Categorias do premio
    '''

    class Meta:
        app_label = 'api'

    #STEP = (
    #    ('0', 'Primeira Etapa'),
    #    ('1', 'Segunda Etapa'),
    #)

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=140, null=True, blank=True)
    #step = models.CharField(max_length=1, choices=STEP)
    edition = models.ForeignKey('Edition', on_delete=models.CASCADE)
    #is_open = models.BooleanField(default=True)

    def __str__(self):
        return u'{0}'.format(self.name)


class Requirement(models.Model):

    '''
    Requisitos da categoria
    '''

    class Meta:
        app_label = 'api'

    text = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return u'{0}'.format(self.category.name)


class UserNomination(models.Model):

    '''
    Resposta do usuario para uma categoria aberta em uma determinada edicao
    '''

    class Meta:
        app_label = 'api'

    response = models.CharField(max_length=140, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    edition = models.ForeignKey('Edition', on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def __str__(self):
        return u'{0}: {1}'.format(self.category.name, self.response)


class AwardNomination(models.Model):

    '''
    Indicados finalistas para a segunda etapa
    '''

    class Meta:
        app_label = 'api'

    name = models.CharField(max_length=64)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    vote = models.ManyToManyField(User, through='UserVote', related_name='vote')

    def __str__(self):
        return u'{0}'.format(self.name)


class UserVote(models.Model):

    '''
    Voto do usuario para indicação de uma categoria
    '''

    class Meta:
        app_label = 'api'

    user = models.ForeignKey(User)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    nomination = models.ForeignKey('AwardNomination', on_delete=models.CASCADE)

    def __str__(self):
        return u'{0}'.format(self.category.name)