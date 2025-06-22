from django.db import models
from django.conf import settings

class Favourite(models.Model):
    pokeapi_id = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    base_experience = models.IntegerField(null=True, blank=True)
    image = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'pokeapi_id'),)


    def __str__(self):
        return (f"{self.name} - Altura: {self.height if self.height else 'Desconocida'} "
                f"(Peso: {self.weight if self.weight else 'Desconocido'}) - "
                f"User: {self.user.username}")
