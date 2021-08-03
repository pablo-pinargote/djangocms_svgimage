from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_svgimage.models import SVGImage


@plugin_pool.register_plugin
class SVGImagePlugin(CMSPluginBase):
    model = SVGImage
    name = _('SVG Image')
    text_enabled = True
    cache = False

    @staticmethod
    def get_render_template(context, instance, placeholder):
        return 'djangocms_svgimage/default/svgimage.html'

    def render(self, context, instance, placeholder):
        inline_styles = ['max-width: 100%;']
        if instance.width:
            inline_styles.append(f'width: {instance.width};')
        if instance.height:
            inline_styles.append(f'height: {instance.height};')
        context['inline_styles'] = ' '.join(inline_styles)
        return super().render(context, instance, placeholder)
