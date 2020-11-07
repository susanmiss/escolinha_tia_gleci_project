from django.db import models

class School(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='main_website/images/escola')
    photo2 = models.ImageField(upload_to='main_website/images/escola')
    photo3 = models.ImageField(upload_to='main_website/images/escola')
    photo4 = models.ImageField(upload_to='main_website/images/escola')
    photo5 = models.ImageField(upload_to='main_website/images/escola')
    photo6 = models.ImageField(upload_to='main_website/images/escola')

    def __str__(self):
        return 'Edite aqui o conteudo da pagina  ' + self.title
    class Meta():
        verbose_name = 'Escola'  
       

class Diferentials(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'Diferenciais'  
    def __str__(self):
        return 'Edite aqui o conteudo da pagina  ' + self.title       

class Visitation(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Visitacao' 
    def __str__(self):
        return 'Edite aqui o conteudo da pagina  ' + self.title     


class Footer(models.Model):
    phone = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)   

    class Meta:
        verbose_name = 'Rodape da Pagina' 
    def __str__(self):
        return 'Edite aqui o conteudo da pagina do Rodape'         