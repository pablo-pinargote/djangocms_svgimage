from cms.models import CMSPlugin
from django.db import models
from filer.fields.file import FilerFileField
from django.utils.translation import gettext_lazy as _


class SVGImage(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    file = FilerFileField(
        verbose_name=_('SVG File'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='svg_file',
    )
    width = models.CharField(
        verbose_name=_('Width'),
        blank=True,
        null=True,
        max_length=255,
        help_text=_(
            'The image width as text in px, % or even em units. '
            'Examples: "720px" "100%"'
        ),
    )
    height = models.CharField(
        verbose_name=_('Height'),
        blank=True,
        null=True,
        max_length=255,
        help_text=_(
            'The image height as text in px, % or even em units. '
            'Examples: "5em" "100%" "auto"'
        ),
    )
    alternative_text = models.CharField(
        verbose_name=_('Alternative Text'),
        blank=True,
        null=True,
        max_length=255,
        help_text=_('Short description for the image.')
    )

    def __str__(self):
        return self.label or str(self.pk)
