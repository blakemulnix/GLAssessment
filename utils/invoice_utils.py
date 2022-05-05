import json
import os
import uuid

from utils.format_utils import FormatUtils

invoice_data_filepath = './data/invoice_data.json'

class InvoiceUtils:

    @staticmethod
    def create_invoice(request_json, base_url):
        new_invoice = request_json
        new_invoice['amount'] = FormatUtils.format_currency_value(new_invoice['amount'])
        new_invoice_id = str(uuid.uuid4())
        new_invoice_url = base_url + '/pay_invoice/' + str(new_invoice_id)
        new_invoice['url'] = new_invoice_url

        with open(invoice_data_filepath, 'r+') as f:
            invoice_data = json.load(f)
            invoice_data['invoices'][new_invoice_id] = new_invoice

            f.seek(0)
            f.write(json.dumps(invoice_data))
            f.truncate()

        return new_invoice_url

    @staticmethod
    def get_invoice(invoice_id):
        with open(invoice_data_filepath, 'r') as f:
            invoice_data = json.load(f)
            invoice = invoice_data['invoices'][invoice_id]
            invoice['amount'] = FormatUtils.format_currency_value(float(invoice['amount']))

        return invoice

    @staticmethod
    def pay_invoice(invoice_id, payment_amount):
        with open(invoice_data_filepath, 'r+') as f:
            invoice_data = json.load(f)
            invoice = invoice_data['invoices'][invoice_id]

            current_balance = float(invoice['amount'])
            remaining_balance = current_balance - payment_amount
            invoice['amount'] = FormatUtils.format_currency_value(remaining_balance)

            invoice_data['invoices'][invoice_id] = invoice

            f.seek(0)
            f.write(json.dumps(invoice_data))
            f.truncate()

        return invoice
