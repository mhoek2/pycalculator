from modules.app.files import FileHandler
from datetime import datetime

class Notes:
    """Contains methods to store notes"""
    def __init__( self, context ) -> None:
        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer
        self.m_gui = context.m_gui
        
        print("Notes init")

    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_notes.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

    def update( self ) -> None:
        #self.m_gui.callGuiMethod()
        return

    def save( self, data ) -> bool:
        """Store note"""

        this_datetime = datetime.now()

        filename = this_datetime.strftime("note_%d_%m_%Y-%H_%M")

        self.file = FileHandler( f"notes/{filename}.txt", True )

        if self.file.setContent( data ) :
           return True
        else:
           return False