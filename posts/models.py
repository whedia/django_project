from django.db import models

class Post(models.Model):
    first_name = models.CharField(max_length=120, help_text='Prénom du joueur')
    last_name = models.CharField(max_length=120, help_text='Nom du joueur')
    cover = models.ImageField(upload_to='images/')
    description = models.TextField(help_text="biographie du joueur")

    def __str__(self):
        return self.first_name