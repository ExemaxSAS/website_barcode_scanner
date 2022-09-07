odoo.define('website_product_template', ['web.ajax'], function (require) {
    "use strict";

    var ajax = require('web.ajax');

    var barcode_container = document.getElementById("barcode_scanner");

    $(document).ready(function () {
        $( "#target" ).submit(function( event ) {
            console.log('E', event);
            event.preventDefault();
            console.log(event);
        });
    });
});