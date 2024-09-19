import locale
import re
from math import isclose

from plusminus import ArithmeticParser

locale.setlocale(locale.LC_ALL, "nl_NL.UTF-8")


class Calculator:
    """Contains methods and variables used for the calculator"""

    def __init__(self, context) -> None:
        """Initialise attributes."""

        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer
        self.m_gui = context.m_gui

        print("Calculator init")
        print("2 + 4,000.88 - 5.24 / 3.948,23 * 4,1234")
        print(self.format_equation_string("2 + 4,000.88 - 5.24 / 3.948,23 * 4,1234"))

    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_notes.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

    def update(self) -> None:
        return

    def format_number_string(self, string):
        """
        Parse strings containing numbers with periods and/or commas.
        The below code tries to determine which style a number is using
        (periods as thousands separators and commas as decimal separator,
        or vice versa) and then returns a string formatted to the number
        format that Python uses (no thousands separators and a period as
        decimal separator).
        """

        # If the string matches European format (comma as decimal separator)
        if re.match(r"^\d{1,3}(\.\d{3})*(,\d+)?$", string):
            # European format: Replace periods (thousands) with nothing, and comma (decimal) with dot
            string = string.replace(".", "").replace(",", ".")

        # If the string matches US format (period as decimal separator)
        elif re.match(r"^\d{1,3}(,\d{3})*(\.\d+)?$", string):
            # US format: Remove commas (thousands) and keep period as decimal separator
            string = string.replace(",", "")

        # Handle cases where there is only one separator type (comma or period)
        elif "," in string and "." not in string:
            # Only comma exists - assume it's a decimal separator if there are two or fewer digits after it
            if len(string.split(",")[1]) <= 2:
                string = string.replace(",", ".")  # Treat as decimal separator
            else:
                string = string.replace(
                    ",", ""
                )  # Treat as thousands separator and remove it

        elif "." in string and "," not in string:
            # Only period exists - assume it's a thousands separator if there are exactly three digits after it
            if len(string.split(".")[1]) != 3:
                pass  # Already in the correct format (period as decimal)
            else:
                string = string.replace(
                    ".", ""
                )  # Treat as thousands separator and remove it

        return string

    def format_equation_string(self, equation: str):
        """Convert numbers in the equation to standardized format with dots as decimal separators."""

        # Regex to find all numbers with possible commas and periods
        number_pattern = r"[\d.,]+"

        # Function to replace each found number with the converted float-like string
        def replace_number(match):
            num_str = match.group(0)
            return str(self.format_number_string(num_str))

        # Replace all numbers in the equation with properly formatted strings
        cleaned_equation = re.sub(number_pattern, replace_number, equation)

        return cleaned_equation

    def parse_equation_string(self, equation: str):
        """This function parses a string containing arithmetic functions."""

        equation = self.format_equation_string(equation)

        return self.format_arithmetic_result(ArithmeticParser().evaluate(equation))

    def format_arithmetic_result(self, result, round_num=10):
        """Format the result of an operation."""

        if isclose(result, round(result)):
            round_num = None
        return round(result, round_num)

    def format_currency_result(self, amount, guilders: bool = True):
        if guilders:
            return f"ƒ {amount:,.2f}".replace(",", ".")[::-1].replace(".", ",", 1)[::-1]
        else:
            return locale.currency(amount, grouping=True)

    def euros_guilders_conversion(self, amount, to_guilders: bool = True):
        """
        Convert euros to dutch guilders. Exchange rate from
        https://www.dnb.nl/en/payments/exchanging-guilder-banknotes/.
        """

        conversion_rate = 2.20371
        amount = self.parse_equation_string(amount)

        if to_guilders:
            return self.format_currency_result(amount * conversion_rate)

        else:
            return self.format_currency_result(amount / conversion_rate, False)
