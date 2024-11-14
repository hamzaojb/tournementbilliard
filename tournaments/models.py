from django.db import models

# Modèle Tournament
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='tournament_images/', blank=True, null=True)  # Nouveau champ

    def __str__(self):
        return self.name

# Modèle Registration
class Registration(models.Model):
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)  # Utilisez le nom du modèle comme chaîne
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)  # Ajout de la contrainte d'unicité
    image = models.ImageField(upload_to='registration_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.tournament.name}"
    
class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='publications/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Relier à l'utilisateur (administrateur)

    def __str__(self):
        return self.title