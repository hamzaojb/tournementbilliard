from django.contrib import admin
from django.utils.html import mark_safe  # Permet d'afficher des balises HTML sécurisées
from .models import Tournament, Registration
from .models import Publication


# Enregistrer le modèle Tournament
admin.site.register(Tournament)

# Enregistrer et personnaliser le modèle Registration dans l'admin
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'tournament', 'image_display')  # Ajout de l'image
    search_fields = ('name', 'email', 'tournament__name')  # Recherche par nom, email et tournoi
    list_filter = ('tournament',)  # Filtrage par tournoi

    # Méthode pour afficher l'image dans l'admin
    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')  # Affichage de l'image
        return "No Image"  # Si l'image n'est pas définie
    image_display.short_description = 'Image'  # Nom de la colonne
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'author']
    search_fields = ['title', 'content']
    list_filter = ['created_at']

# Enregistrer le modèle Publication dans l'admin
admin.site.register(Publication, PublicationAdmin)