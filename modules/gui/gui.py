from modules.gui.textInput import TextInput
from modules.gui.button import Button

import pygame

class Gui:
    """Containing methods for various use cases of the application"""
    def __init__( self, context ) -> None:
        self.m_context = context
        self.m_settings = context.m_settings
        self.m_renderer = context.m_renderer

        self.text_input_group = pygame.sprite.Group()
        self.button_group = []

        # tabs defines
        self.TAB_CALCULATOR     = 0
        self.TAB_NOTES          = 1
        self.TAB_KOPPELCODE     = 2

        self.tab_index = self.TAB_NOTES

        print("Gui init")

    # Example on how to call functions from other modules:
    # self.m_context.m_gui.functionName()
    # self.m_context.m_notes.functionName()
    # self.m_context.m_calculator.functionName()
    # self.m_context.m_koppelcode.functionName()

    #
    # globals
    #
    def addTextInput( self, object ) -> None:
        self.text_input_group.add( object )

    def addButton( self, object ) -> None:
        self.button_group.append( object )

    def draw( self ) -> None:
        """Draw GUI and the active tab content"""
        self.drawTab()

    #
    # tabbing system
    #
    def clearTabContent( self ) -> None:
        self.text_input_group.empty()
        self.button_group.clear()

    def openTab( self, index ) -> None:
        """Handle switching between tabs"""
        if self.tab_index != index:
            self.clearTabContent()
            self.tab_index = index

        if self.tab_index == self.TAB_CALCULATOR:
            self._initCalculator()

        elif self.tab_index == self.TAB_NOTES:
            self._initNotes()

        elif self.tab_index == self.TAB_KOPPELCODE:
            self._initKoppelcode()

    def drawTab( self ) -> None:
        """Call to current open tab drawing method"""
        if self.tab_index == self.TAB_CALCULATOR:
            self._drawCalculator()

        elif self.tab_index == self.TAB_NOTES:
            self._drawNotes()

        elif self.tab_index == self.TAB_KOPPELCODE:
            self._drawKoppelcode()


    #
    # debug code
    #
    def _handle_key_down( self, event ) -> None:
        """DEBUG: Handle key-down"""
        if event.key == pygame.K_c:
            self.openTab( self.TAB_CALCULATOR )

        elif event.key == pygame.K_n:
            self.openTab( self.TAB_NOTES )

        elif event.key == pygame.K_k:
            self.openTab( self.TAB_KOPPELCODE )

    def button_group_event_handler( self, event ) -> None:
        """Handle event states for mousedown on buttons"""
        if event.button == 1:
            pos = pygame.mouse.get_pos()
            for b in self.button_group:
                if b.rect.collidepoint(pos):
                    b.call_back()

    def event_handler( self, event_list ) -> None:
        for event in event_list:
            # used for debug code
            if event.type == pygame.KEYDOWN:
                self._handle_key_down( event )

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # handle event for all buttons
                self.button_group_event_handler( event )

        # handle events for all text input fields
        self.text_input_group.update( event_list )

    #
    # calculator
    #
    def _initCalculator( self ) -> None:
        """This gets executed when tab opens"""
        return

    def _drawCalculator( self ) -> None:
        """Update method every frame"""
        return

    #
    # koppelcode
    #
    def _initKoppelcode( self ) -> None:
        """This gets executed when tab opens"""
        return

    def _drawKoppelcode( self ) -> None:
        """Update method every frame"""
        return

    #
    # notes
    #
    def fn2( self ) -> None:
        print("button")

    def _initNotes( self ) -> None:
        """This gets executed when tab opens"""
        note = TextInput(10, 50, 380, self.m_renderer.m_font_48)
        self.addTextInput( note )

        button = Button((200, 150), (100, 50), (220, 220, 220), (255, 0, 0), self.fn2, 'Opslaan')
        self.addButton( button )
        

    def _drawNotes( self ) -> None:
        """Update method every frame"""
        # text input fields
        self.text_input_group.draw( self.m_renderer.m_screen )

        # buttons
        for button in self.button_group:
            button.draw( self.m_renderer.m_screen )

        return

    def getNote( self ) -> None:
        """Return text in note input field"""
        return self.note.text

    def clearNote( self ) -> None:
        """Reset text to empty state"""
        self.note.reset()

    def saveNote( self ) -> None:
        """Call to Note module to save current text in input field"""
        self.m_context.m_notes.save( self.getNote() )
        self.clearNote()
	def callGuiMethod( self ) -> None:
		print(".")