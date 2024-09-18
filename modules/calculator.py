import locale
from plusminus import ArithmeticParser
from math import isclose

locale.setlocale(locale.LC_ALL, "nl_NL.UTF-8")


class Calculator:
    """Contains methods and variables used for the calculator"""

    def __init__( self, context ) -> None:
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

    def update( self ) -> None:
        return

    def parse_arithmetic_string(self, arithmetic: str):
        """This function parses a string containing arithmetic functions."""
        if "," in arithmetic:
            arithmetic = arithmetic.replace(",", ".")

        return self.format_arithmetic_result(ArithmeticParser().evaluate(arithmetic))

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

    def add(self, first_number, second_number):
        """Add two numbers to each other."""

        return self.format_arithmetic_result(first_number + second_number)

    def subtract(self, first_number, second_number):
        """Subtract two numbers from each other."""

        return self.format_arithmetic_result(first_number - second_number)

    def multiply(self, first_number, second_number):
        """Multiply a number by another number."""

        return self.format_arithmetic_result(first_number * second_number)

    def divide(self, first_number, second_number):
        """Divide two numbers by each other."""
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return self.format_arithmetic_result(first_number / second_number)

    def powerof(self, first_number, second_number):
        """One number to the power of another number."""

        return self.format_arithmetic_result(pow(first_number, second_number))

    def euros_guilders_conversion(self, amount, to_guilders: bool = True):
        """
        Convert euros to dutch guilders. Exchange rate from
        https://www.dnb.nl/en/payments/exchanging-guilder-banknotes/.
        """
        conversion_rate = 2.20371

        if to_guilders:
            return self.format_currency_result(amount * conversion_rate)

        else:
            return self.format_currency_result(amount / conversion_rate, False)


def test():
    """Test the Calculator class."""

    calc = Calculator()
    print(f"Addition (539 + 4,345):                  {calc.add(539, 4.345)}")
    print(f"Subtraction (2347 - 5000):               {calc.subtract(2347, 5000)}")
    print(f"Multiplication (2,3 * 55):               {calc.multiply(55, 2.3)}")
    print(f"Division (30 / 0,3):                     {calc.divide(30, 0.3)}")
    print(f"More complicated division (30 / 0,7):    {calc.divide(30, 0.7)}")
    print(
        f"Euros to guilders (1):                   {calc.euros_guilders_conversion(1000000000000000000000000)}"
    )
    print(
        f"Guilders to euros (1):                   {calc.euros_guilders_conversion(1, False)}"
    )
    print(f"6 to the power of 3:                     {calc.powerof(6, 3)}")
    # print(f"Parsing 2*5++------------------------,9: {calc.parse_arithmetic_string("2*5++------------------------,9")}")


# test()
