from odoo import http
from odoo.http import request, Controller, route
import json
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Zaitk_Midd(http.Controller):
    @http.route('/get_product', type="json", auth='public', csrf=False)
    def get_all_products(self):
        prod_rec = request.env['product.product'].search([])
        prods = []
        for rec in prod_rec:
            vals = {
                'id': rec.id,
                'name': rec.display_name,
                'uom_id': rec.uom_id.id,
                'uom': rec.uom_id.name,
                'list_price': rec.list_price,
            }

            prods.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': prods,
        }
        return data


    @http.route('/get_category', type="json", auth='public', csrf=False)
    def get_all_category(self):
        read_rec = request.env['product.category'].search([])
        parms = []
        for rec in read_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            parms.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': parms,
        }
        return data

    @http.route('/get_units', type="json", auth='public', csrf=False)
    def get_all_units(self):
        read_rec = request.env['uom.uom'].search([])
        parms = []
        for rec in read_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            parms.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': parms,
        }
        return data

    @http.route('/get_workshop', type="json", auth='public', csrf=False)
    def get_all_workshop(self):
        read_rec = request.env['operating.unit'].search([])
        parms = []
        for rec in read_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'code': rec.code,
                'active': rec.active

            }
            parms.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': parms,
        }
        return data

    @http.route('/get_attribute', type="json", auth='public', csrf=False)
    def get_all_attribute(self):
        read_rec = request.env['product.attribute'].search([])
        parms = []
        for rec in read_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,

            }
            parms.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': parms,
        }
        return data

    @http.route('/get_attribute_val', type="json", auth='public', csrf=False)
    def get_all_attribute_val(self):
        read_rec = request.env['product.attribute.value'].search([])
        parms = []
        for rec in read_rec:
            vals = {
                'id': rec.id,
                'attribute': rec.attribute_id,
                'name': rec.name,
                'attribute_line': rec.pav_attribute_line_ids,
            }
            parms.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': parms,
        }
        return data

