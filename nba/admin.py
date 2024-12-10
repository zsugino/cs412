# File: admin.py
# Author: Zai Sugino (xysugino@bu.edu), 12/10/2024
# Description: Admin to register model to admin

from django.contrib import admin

# Register your models here.
from .models import Player, Ranking, DreamTeam, Review, PlayerReview
admin.site.register(Player)
admin.site.register(Ranking)
admin.site.register(DreamTeam)
admin.site.register(Review)
admin.site.register(PlayerReview)





