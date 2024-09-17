class KoppelCode:
    """Contains methods used to create a random uppercase string of letters"""
    def __init__( self, context ) -> None:
        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer
        self.m_gui = context.m_gui

        print("KoppelCode init")

    def update( self ) -> None:
        return