# Generated by Django 4.2.16 on 2024-11-18 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0002_alter_player_draft_number_alter_player_draft_round"),
    ]

    operations = [
        migrations.RemoveField(model_name="player", name="draft_number",),
        migrations.RemoveField(model_name="player", name="draft_round",),
    ]
