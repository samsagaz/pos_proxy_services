odoo.define('pos_proxy_service.screens', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const POSValidateOverride = PaymentScreen =>
        class extends PaymentScreen {
            /**
             * @override
             */

            async validateOrder(isForceValidate) {
                
                if (this.env.pos.config.use_fiscal_printer){
                var valid_fiscal = true;
                console.log("uno");
                var paymentlines = this.env.pos.get_order().get_paymentlines();
                console.log("dos");
                console.log(paymentlines['0']);
                if(!paymentlines['0']) valid_fiscal = false;
                if (valid_fiscal){
                //$('.pos-receipt-container').addClass('oe_hidden');
                var response = this.env.pos.print_pos_ticket();
                }
                




                
                }

                console.log("tres");
                console.log('POSValidateOverride::validateOrder(): successfully overridden');
                await super.validateOrder(isForceValidate);
                // Add your code
            }
        };

    Registries.Component.extend(PaymentScreen, POSValidateOverride);

    return PaymentScreen;
});