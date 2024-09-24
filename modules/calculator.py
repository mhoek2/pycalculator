import locale
import re
from math import isclose

from plusminus import ArithmeticParser


class Calculator:
    """Contains methods and variables used for the calculator"""

    def __init__(self, context) -> None:
        """Initialise attributes."""

        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer
        self.m_gui = context.m_gui

        print("Calculator init")

    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_notes.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

    def update(self) -> None:
        return

    def format_number_string(self, number_string: str):
        """
        Parse strings containing numbers with periods and/or commas.
        The below code tries to determine which style a number is using
        (periods as thousands separators and commas as decimal separator,
        or vice versa) and then returns a string formatted to the number
        format that Python uses (no thousands separators and a period as
        decimal separator).
        """

        # If the string matches European format (comma as decimal separator)
        if re.match(r"^\d{1,3}(\.\d{3})*(,\d+)?$", number_string):
            # European format: Replace periods (thousands) with nothing, and comma (decimal) with dot
            number_string = number_string.replace(".", "").replace(",", ".")

        # If the string matches US format (period as decimal separator)
        elif re.match(r"^\d{1,3}(,\d{3})*(\.\d+)?$", number_string):
            # US format: Remove commas (thousands) and keep period as decimal separator
            number_string = number_string.replace(",", "")

        # Handle any other cases
        elif any(i in number_string for i in ",."):
            sep_count = len(re.findall(r"[,.]", number_string))
            split_number_string = re.split(r"[,.]+", number_string)

            if len(split_number_string[-1]) != 3 or sep_count == 1:
                if sep_count > 1:
                    sep_count -= 1
                elif sep_count == 1:
                    sep_count = -1

            number_string = re.sub(r"[,.]+", "", number_string, sep_count).replace(
                ",", "."
            )
        return number_string

    def format_equation_string(self, equation: str):
        """Convert numbers in the equation to standardized format with dots as decimal separators."""

        # Function to replace each found number with the converted float-like string
        def replace_number(match):
            num_str = match.group(0)
            return str(self.format_number_string(num_str))

        # Replace all numbers in the equation with properly formatted strings
        cleaned_equation = re.sub(r"[\d.,]+", replace_number, equation)

        return cleaned_equation

    def parse_equation_string(self, equation: str):
        """This function parses a string containing arithmetic functions."""

        # Handle empty strings
        if not equation:
            return "Lege berekening"

        equation = self.format_equation_string(equation)

        # Handle any errors that may occur while parsing an equation
        try:
            return self.format_arithmetic_result(ArithmeticParser().evaluate(equation))
        except:
            return "Ongeldig"

    def format_arithmetic_result(self, result, round_num=10):
        """Format the result of an operation."""

        if isclose(result, round(result)):
            round_num = None
        return round(result, round_num)

    def format_currency_result(self, amount, guilders: bool = True):
        """Format the result of a currency conversion."""
        if guilders:
            return f"ƒ {amount:,.2f}".replace(",", ".")[::-1].replace(".", ",", 1)[::-1]
        else:
            locale.setlocale(locale.LC_ALL, "nl_NL.UTF-8")
            return locale.currency(amount, grouping=True)

    def euros_guilders_conversion(self, amount, to_guilders: bool = True):
        """
        Convert euros to Dutch guilders. Exchange rate from
        https://www.dnb.nl/en/payments/exchanging-guilder-banknotes/.
        Assume a conversion is being done from euros to guilders by default.
        """

        if not amount:
            return "Leeg bedrag"

        conversion_rate = 2.20371
        amount = self.parse_equation_string(amount)

        if to_guilders:
            return self.format_currency_result(amount * conversion_rate)

        else:
            return self.format_currency_result(amount / conversion_rate, False)

    def print_formatted_equations_test(self, equations):
        """
        Print each equation (and, by extension, equation) along with its parsed value,
        after being processed by format_equation_string.
        """
        for equation in equations:
            parsed_equation = self.format_equation_string(equation)
            print(f"Original: {equation} -> Parsed: {parsed_equation}")
