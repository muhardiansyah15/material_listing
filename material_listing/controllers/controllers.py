# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.exceptions import ValidationError

class MaterialController(http.Controller):

    @http.route('/materials', auth='user', type='http')
    def index(self, **kw):
        materials = request.env['material.material'].sudo().search([])
        return request.render('material_listing.materials', {
            'materials': materials,
        })

    @http.route('/materials/create', auth='user', type='http', methods=['GET', 'POST'])
    def create(self, **kw):
        error = False
        if kw.get('submit'):
            try:
                request.env['material.material'].sudo().create({
                    'code': kw['code'],
                    'name': kw['name'],
                    'type': kw['type'],
                    'buy_price': float(kw['buy_price']),
                    'supplier_id': int(kw['supplier_id']),
                })
            except ValidationError:
                error = _('Error: Please fill in all required fields and make sure the buy price is at least 100.')
        suppliers = request.env['supplier.supplier'].sudo().search([])
        return request.render('material_listing.material_create', {
            'suppliers': suppliers,
            'error': error,
        })

    @http.route('/materials/update/<int:material_id>', auth='user', type='http', methods=['GET', 'POST'])
    def update(self, material_id, **kw):
        error = False
        material = request.env['material.material'].sudo().browse(material_id)
        if kw.get('submit'):
            try:
                material.write({
                    'code': kw['code'],
                    'name': kw['name'],
                    'type': kw['type'],
                    'buy_price': float(kw['buy_price']),
                    'supplier_id': int(kw['supplier_id']),
                })
            except ValidationError:
                error = _('Error: Please fill in all required fields and make sure the buy price is at least 100.')
        suppliers = request.env['supplier.supplier'].sudo().search([])
        return request.render('material_listing.material_update', {
            'material.material': material,
            'suppliers': suppliers,
            'error': error,
        })

    @http.route('/materials/delete/<int:material_id>', auth='user', type='http', methods=['POST'])
    def delete(self, material_id, **kw):
        request.env['material.material'].sudo().browse(material_id).unlink()
        return request.redirect('/materials')