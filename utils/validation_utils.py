
class ValidationUtils:

    @staticmethod
    def validate_invoice_request(request):
        try:
            json = request.json
        except Exception as e:
            print(e)
            return {'errors': [{'code': 100, 'description': 'Could not parse JSON from request body'}]}

        for key in ['title', 'description', 'amount']:
            if key not in json.keys():
                return {'errors': [{'code': 101, 'description': 'Request body is missing {}'.format(key)}]}

        for key in ['title', 'description']:
            if type(json[key]) is not str:
                return {'errors': [{'code': 102, 'description': '{} must be string'.format(key)}]}

        if type(json['amount']) is not float and type(json['amount']) is not int:
            return {'errors': [{'code': 102, 'description': 'amount must be a float or an integer'.format(key)}]}

        if float(json['amount']) < 0:
            return {'errors': [{'code': 103, 'description': 'amount cannot be negative'}]}

        if float(json['amount']) == 0:
            return {'errors': [{'code': 104, 'description': 'amount cannot be zero'}]}

        if str(json['amount'])[::-1].find('.') > 2:
            return {'errors': [{'code': 105, 'description': 'amount cannot have fractional cents'}]}