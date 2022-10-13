from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AnasaabConfig(AppConfig):
    name = "shajra.ansaab"
    verbose_name = _("Ansaab")

    def ready(self):
        try:
            import shajra.ansaab.signals  # noqa F401
        except ImportError:
            pass
