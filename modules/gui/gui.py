class Gui:
	"""Containing methods for various use cases of the application"""
	def __init__( self, context ) -> None:
		self.m_context = context
		self.m_settings = context.m_settings
		self.m_renderer = context.m_renderer

		print("Gui init")

    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_notes.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

	def update( self ) -> None:
		return

	def callGuiMethod( self ) -> None:
		print(".")