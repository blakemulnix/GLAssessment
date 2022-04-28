currency_format = '{:.2f}'


class FormatUtils:

    @staticmethod
    def format_currency_value(value):
        return currency_format.format(value)
