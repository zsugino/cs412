# Generated by Django 4.2.16 on 2024-11-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Voter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("voter_id_number", models.TextField()),
                ("first_name", models.TextField()),
                ("last_name", models.TextField()),
                ("date_of_birth", models.DateField()),
                ("date_of_registration", models.DateField()),
                ("party_affiliation", models.TextField()),
                ("precinct_number", models.TextField()),
                ("ra_street_number", models.TextField()),
                ("ra_street_name", models.TextField()),
                ("ra_apartment_number", models.TextField()),
                ("ra_zip_code", models.TextField()),
                ("v20state", models.BooleanField()),
                ("v21town", models.BooleanField()),
                ("v21primary", models.BooleanField()),
                ("v22general", models.BooleanField()),
                ("v23town", models.BooleanField()),
                ("voter_score", models.IntegerField()),
            ],
        ),
    ]
