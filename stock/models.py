from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone

# Create your models here.


class Article(models.Model):
    code=models.IntegerField(blank=True)
    nom = models.CharField(max_length=20)
    quantity=models.IntegerField(null=True)
    prix_achat=models.IntegerField(null=True)
    # quantité_en_vrac ===== الكميـــة فـــــــــــي الجملـــــــــــة 

    def __str__(self):
        return self.nom
 

class Commande(models.Model):
    produit = models.ManyToManyField(Article)
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)

    def __str__(self):
        return f"la commande de l'utilisateur {self.user}"
