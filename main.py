import json

from flask import Flask, request, render_template

from utils.validation_utils import ValidationUtils
from utils.format_utils import FormatUtils
from utils.invoice_utils import InvoiceUtils

app = Flask(__name__)

base_url = 'localhost:5000/'


@app.route('/invoices', methods=['POST'])
def invoices():
    errors = ValidationUtils.validate_invoice_request(request)

    if errors:
        return json.dumps(errors), 400

    new_invoice_url = InvoiceUtils.create_invoice(request.json, base_url)
    response_data = {'data': {'url': new_invoice_url}}

    return json.dumps(response_data), 200


@app.route('/pay_invoice/<invoice_id>', methods=['GET', 'POST'])
def pay_invoice(invoice_id):
    if request.method == 'POST':
        payment_amount = float(request.form.get("payment_amount"))
        invoice = InvoiceUtils.pay_invoice(invoice_id, payment_amount)
        remaining_balance = float(invoice['amount'])

        if remaining_balance <= 0:
            return render_template('payment_complete.html',
                                   invoice=invoice)
        else:
            return render_template('pay_invoice.html',
                                   invoice_id=invoice_id,
                                   invoice=invoice,
                                   payment_made=FormatUtils.format_currency_value(payment_amount))

    elif request.method == 'GET':
        invoice = InvoiceUtils.get_invoice(invoice_id)
        remaining_balance = float(invoice['amount'])

        if remaining_balance <= 0:
            return render_template('payment_complete.html',
                                   invoice=invoice)
        else:
            return render_template('pay_invoice.html',
                                   invoice_id=invoice_id,
                                   invoice=invoice,
                                   payment_made=None)


if __name__ == '__main__':
    app.run()
