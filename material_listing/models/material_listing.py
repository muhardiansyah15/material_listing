# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


TYPE_SELECTION = [
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ]

class Supplier(models.Model):
    _name = 'supplier.supplier'
    _description = 'Supplier Information'

    name = fields.Char(string='Supplier Name', required=True)
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone Number')
    
    

class Material(models.Model):
    _name = 'material.material'
    _description = 'Material Information'

    name = fields.Char(string='Material Name', required=True)
    code = fields.Char(string='Material Code', required=True)
    type = fields.Selection(selection=TYPE_SELECTION, string='Material Type', required=True)
    buy_price = fields.Float(string='Material Buy Price', required=True, default=0.0)
    supplier_id = fields.Many2one(comodel_name='supplier.supplier', string='Supplier', required=True)

    @api.constrains('buy_price')
    def _buy_price_validation(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError(_('Buy price should not be less than 100.'))