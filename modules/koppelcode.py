import random
from turtledemo.chaos import jumpto

class KoppelCode:
    """Contains methods used to create a random uppercase string of letters"""
    def __init__( self, context ) -> None:
        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer
        self.m_gui = context.m_gui
        self.alphabet = (
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W",
        "X", "Y", "Z")

        print("KoppelCode init")

    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_notes.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

    def update( self ) -> None:
        random_code = self.get_random_code(4)
        print(random_code)
        return

    def get_random_code(self, num_letters):
        random_code2 = ""
        for i in range(0, num_letters):
            random_letter = self.alphabet[random.randint(0,24)]
            random_code2 += random_letter
        return random_code2
