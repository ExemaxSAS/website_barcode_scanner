# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.exceptions import AccessError, UserError
from odoo.http import request

class OdooWebsite(http.Controller):

    @http.route(['/barcode_scanner'], auth="public", website=True)
    def barcode_scanner(self):
        return request.render('website_barcode_scanner.barcode_scanner', {})

    @http.route(['/get_product_barcode'], type='json', auth="public", website=True)
    def get_related_products(self, barcode=False, offset=0):
        prod = http.request.env['product.template'].sudo().search([('barcode','=', barcode)], limit=1)
        return prod.name
