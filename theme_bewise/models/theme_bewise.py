from odoo import models


class ThemeBewise(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bewise_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_headline')

        self.enable_view('website.option_ripple_effect')
