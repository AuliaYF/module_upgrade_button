from odoo import api, fields, models


class InheritIrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.multi
    def _button_immediate_function(self, function):
        super(InheritIrModuleModule, self)._button_immediate_function(function)

        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }
