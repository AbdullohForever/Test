# Generated by Django 4.1.7 on 2023-06-23 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
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
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "INACTIVE"), (1, "ACTIVE"), (2, "OTHER")],
                        default=1,
                        verbose_name="Holati",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="yaratilgan vaqt"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="tahrirlangan vaqt"
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Option",
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
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "INACTIVE"), (1, "ACTIVE"), (2, "OTHER")],
                        default=1,
                        verbose_name="Holati",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="yaratilgan vaqt"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="tahrirlangan vaqt"
                    ),
                ),
                ("text", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Variant",
                "verbose_name_plural": "Variantlar",
                "ordering": ["question", "text"],
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "INACTIVE"), (1, "ACTIVE"), (2, "OTHER")],
                        default=1,
                        verbose_name="Holati",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="yaratilgan vaqt"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="tahrirlangan vaqt"
                    ),
                ),
                ("text", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Savol",
                "verbose_name_plural": "Savollar",
                "ordering": ["text"],
            },
        ),
        migrations.DeleteModel(
            name="Test",
        ),
        migrations.AddField(
            model_name="option",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="option",
                to="main.question",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="option",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.option"
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="main.question"
            ),
        ),
    ]
