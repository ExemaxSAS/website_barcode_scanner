# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.exceptions import AccessError, UserError
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class OdooWebsite(http.Controller):

    @http.route(['/barcode_scanner', '/barcode_scanner/<int:barcode>'], auth="public", website=True)
    def barcode_scanner(self, barcode=False):
        if not barcode:
            return request.render('website_barcode_scanner.barcode_scanner', {'product': False, 'combination': False})
        else:
            prod = http.request.env['product.template'].sudo().search([('barcode', '=', barcode)], limit=1)
            pricelist = http.request.env['product.pricelist'].sudo().search([('id', '=', 1)], limit=1)
            combination = prod._get_first_possible_combination()
            combination_info = prod._get_combination_info(combination=combination, only_template=True, add_qty=1, pricelist=pricelist)

            return request.render('website_barcode_scanner.barcode_scanner', {'product': prod, 'combination': combination_info, 'pricelist': pricelist})

    @http.route(['/get_product_barcode'], type='http', auth="public", website=True)
    def get_related_products(self, **kw):
        if kw['search']:
            return request.redirect('/barcode_scanner/' + kw['search'])
        else:
            return request.redirect('/barcode_scanner')
