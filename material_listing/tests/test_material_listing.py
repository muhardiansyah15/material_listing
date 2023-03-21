# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super().setUp()

        # Create test data for Supplier
        self.supplier_1 = self.env['supplier.supplier'].create({'name': 'Supplier 1'})
        self.supplier_2 = self.env['supplier.supplier'].create({'name': 'Supplier 2'})

        # Create test data for Material Listing
        self.material_1 = self.env['material.material'].create({
            'code': 'M001',
            'name': 'Material 1',
            'type': 'fabric',
            'buy_price': 150.0,
            'supplier_id': self.supplier_1.id,
        })
        self.material_2 = self.env['material.material'].create({
            'code': 'M002',
            'name': 'Material 2',
            'type': 'jeans',
            'buy_price': 200.0,
            'supplier_id': self.supplier_1.id,
        })
        self.material_3 = self.env['material.material'].create({
            'code': 'M003',
            'name': 'Material 3',
            'type': 'cotton',
            'buy_price': 300.0,
            'supplier_id': self.supplier_2.id,
        })

    def test_create_material(self):
        # Test creating a new material
        material = self.env['material.material'].create({
            'code': 'M004',
            'name': 'Material 4',
            'type': 'fabric',
            'buy_price': 120.0,
            'supplier_id': self.supplier_2.id,
        })
        self.assertTrue(material)

    def test_update_material(self):
        # Test updating an existing material
        self.material_1.write({
            'name': 'Updated Material 1',
            'supplier_id': self.supplier_2.id,
        })
        self.assertEqual(self.material_1.name, 'Updated Material 1')
        self.assertEqual(self.material_1.supplier_id, self.supplier_2)

    def test_delete_material(self):
        # Test deleting an existing material
        self.material_2.unlink()
        materials = self.env['material.material'].search([])
        self.assertEqual(len(materials), 2)

    def test_check_buy_price_constraint(self):
        # Test the constraint that buy price must be greater than or equal to 100
        with self.assertRaises(ValidationError):
            self.env['material.material'].create({
                'code': 'M004',
                'name': 'Material 4',
                'type': 'fabric',
                'buy_price': 50.0,
                'supplier_id': self.supplier_2.id,
            })