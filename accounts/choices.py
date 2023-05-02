from django.db.models import TextChoices

class RiskProfileChoices(TextChoices):
    CONSERVADOR = 'Conservador', 'Conservador'
    MODERADO = 'Moderado', 'Moderado'
    ARROJADO = 'Arrojado', 'Arrojado'