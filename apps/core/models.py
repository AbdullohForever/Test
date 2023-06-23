from django.db import models


class Status(models.IntegerChoices):
    INACTIVE = 0, "INACTIVE"
    ACTIVE = 1, "ACTIVE"
    OTHER = 2, "OTHER"


class TimeStampedModel(models.Model):
	"""
	An abstract base class model that provides self-
	updating ``created_at``, ``modified_at``, ``status`` fields.
	"""

	# status for temporarily deletion or smth
	status = models.PositiveSmallIntegerField(
		choices = Status.choices,
		default = Status.ACTIVE,
		verbose_name = "Holati"
	)

	created_at = models.DateTimeField(
		auto_now_add=True,
		# default=timezone.now,
		verbose_name = "yaratilgan vaqt"
		)

	modified_at = models.DateTimeField(
		auto_now=True,
		# default=timezone.now,
		verbose_name = "tahrirlangan vaqt"
		)

	class Meta:
		abstract = True
		ordering = ('created_at',)

