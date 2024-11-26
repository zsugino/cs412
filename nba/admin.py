from django.contrib import admin

# Register your models here.
from .models import Player, Ranking, DreamTeam, Review
admin.site.register(Player)
admin.site.register(Ranking)
admin.site.register(DreamTeam)
admin.site.register(Review)




