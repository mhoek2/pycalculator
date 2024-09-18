from modules.app.files import FileHandler

class FileStore:
    """Contains methods to store files containing notes"""
    def __init__( self, context ) -> None:
        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer
        self.m_gui = context.m_gui
        
        print("FileStore init")
        self.save("teest")


    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_filestore.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

    def update( self ) -> None:
        self.m_gui.callGuiMethod()
        return

    def save( self, data ) -> bool:
        """Store note"""

        self.file = FileHandler( "test.txt", True )

        if self.file.setContent( data ) :
           return True
        else:
           return False