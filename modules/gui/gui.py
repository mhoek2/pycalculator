class Gui:
	"""Containing methods for various use cases of the application"""
	def __init__( self, context ) -> None:
		self.m_context = context
		self.m_settings = context.m_settings
		self.m_renderer = context.m_renderer

		print("Gui init")

	def update( self ) -> None:
		return

	def callGuiMethod( self ) -> None:
		return
		#print(".")