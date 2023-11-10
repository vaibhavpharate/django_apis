# Generated by Django 4.2.4 on 2023-11-10 08:57

import apis.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apis", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="clients",
            name="plans",
            field=models.ForeignKey(
                default=apis.models.Plans.get_default_name,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_plans",
                to="apis.plans",
                to_field="plan_type",
            ),
        ),
    ]
