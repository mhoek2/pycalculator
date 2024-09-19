from modules.gui.textInput import TextInput
from modules.gui.button import Button, CalculatorButton

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
        self.TAB_GULDENS        = 3

        self.tab_index = self.TAB_NOTES

        # koppelcode
        self.koppel_code_text = ""

        # note
        self.note = None            # text input field

        # background
        self.loadBackground()

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

    #
    # background
    #
    def loadBackground( self ) -> None:
       self.m_background = pygame.image.load( self.m_settings.m_background_image_path )
       self.m_background = pygame.transform.scale(  self.m_background, self.m_settings.m_resolution )
       self.m_background_rect = self.m_background.get_rect()
       self.m_background_rect.topleft = self.m_renderer.m_screen_rect.topleft

    def drawBackground( self ) -> None:
         self.m_renderer.m_screen.blit( self.m_background, self.m_background_rect )

    def draw( self ) -> None:
        """Draw GUI and the active tab content"""
        self.drawBackground()

        # text input fields
        self.text_input_group.draw( self.m_renderer.m_screen )

        # buttons
        for button in self.button_group:
            button.draw( self.m_renderer.m_screen )

        self.drawTab()

    #
    # tabbing system
    #
    def drawTabs( self ) -> None:
        position_y = 20
        position_x = 37

        tab_notes = Button((position_x, position_y), (75, 50), 
                           (220, 220, 220), (255, 0, 0), self.openNotesTab, 'Notities')
        self.addButton( tab_notes )
        position_x += 110
 
        tab_calculator = Button((position_x, position_y), (130, 50), 
                                (220, 220, 220), (255, 0, 0), self.openCalculatorTab, 'Rekenmachine')
        self.addButton( tab_calculator )
        position_x += 132

        tab_koppelcode = Button((position_x, position_y), (120, 50), 
                                (220, 220, 220), (255, 0, 0), self.openKoppelcodeTab, 'koppelcode')
        self.addButton( tab_koppelcode )
        position_x += 90
        
        tab_guldens = Button((position_x, position_y), (64, 50), 
                                (220, 220, 220), (255, 0, 0), self.openGuldensTab, 'ƒ ↔ €')
        self.addButton( tab_guldens )
  
    def openNotesTab( self ) -> None:
        self.openTab( self.TAB_NOTES )

    def openCalculatorTab( self ) -> None:
        self.openTab( self.TAB_CALCULATOR )

    def openKoppelcodeTab( self ) -> None:
        self.openTab( self.TAB_KOPPELCODE )
        
    def openGuldensTab( self ) -> None:
        self.openTab( self.TAB_GULDENS )

    def clearTabContent( self ) -> None:
        self.text_input_group.empty()
        self.button_group.clear()
        self.drawTabs()

    def openTab( self, index ) -> None:
        """Handle switching between tabs"""
        if self.tab_index != index:
            self.clearTabContent()
            self.tab_index = index
        else:
            return

        if self.tab_index == self.TAB_CALCULATOR:
            self._initCalculator()

        elif self.tab_index == self.TAB_NOTES:
            self._initNotes()

        elif self.tab_index == self.TAB_KOPPELCODE:
            self._initKoppelcode()
        
        elif self.tab_index == self.TAB_GULDENS:
            self._initGuldens()

    def drawTab( self ) -> None:
        """Call to current open tab drawing method"""
        if self.tab_index == self.TAB_CALCULATOR:
            self._drawCalculator()

        elif self.tab_index == self.TAB_NOTES:
            self._drawNotes()

        elif self.tab_index == self.TAB_KOPPELCODE:
            self._drawKoppelcode()
        
        elif self.tab_index == self.TAB_GULDENS:
            self._drawGuildersConversion()


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
    def addNumberToEquation( self, symbol ) -> None:
        """Add number 1-9 to the equation"""
        self.equation += symbol

    def addSymbolToEquation( self, symbol ) -> None:
        """Add a modifier or '.', ',' symbol to te equation
        Also prevent starting with zero digit"""
        if len( self.equation ) > 0:
            # check for modifiers
            if self.equation[-1] in self.modifiers:
                return

            # check for '.', ',', skip '0'
            if self.equation[-1] in self.extra[1:]:
                return
        else:
            # none are allowed at the start of the equation
            return

        self.equation += symbol

    def clearEquation( self ) -> None:
        """Reset the equation to be empty string"""
        self.equation = ""

    def calculate( self ) -> None:
        """Ask the calculator module to evaluate the outcome of the equation"""
        print( f"calculate: {self.m_context.m_calculator.parse_arithmetic_string(self.equation)}")
        return

    def _initCalculator( self ) -> None:
        """This gets executed when tab opens"""

        self.equation = ""

        row = 0
        column = 0
        total_columns = 0;
        total_rows = 0;

        button_width = 60
        button_height = 60
        button_margin_x = button_width + 10
        button_margin_y = button_height + 10

        self.modifier_letters = ["+", "-", "x", ":"]
        self.modifiers = ["+", "-", "*", "/"]
        self.extra = ["0", ".", ","]

        button_columns = 4

        keypad_center = ( button_columns * button_margin_x ) / 2

        positon_x_start = ( self.m_renderer.m_screen_rect.width / 2 ) - keypad_center
        positon_y_start = 200


        # draw numeric buttons
        for i in range(1,10):
            position_y = positon_y_start + (row * button_margin_y)
            position_x = positon_x_start + (column * button_margin_x)

            button = CalculatorButton((position_x, position_y), (button_width, button_height), (220, 220, 220), (255, 0, 0), self.addNumberToEquation, f"{i}", f"{i}")
            self.addButton( button )

            column += 1
            
            if i % 3 == 0:
                row += 1
                total_columns += 1
                total_rows += 1
                column = 0
        
        # draw modifiers
        for i in range(0, len( self.modifiers ) ):
            position_y = positon_y_start + (i * button_margin_y)
            position_x = positon_x_start + (total_columns * button_margin_x)
            button = CalculatorButton((position_x, position_y), (button_width, button_height), (220, 220, 220), (255, 0, 0), self.addSymbolToEquation, f"{self.modifiers[i]}", f"{self.modifier_letters[i]}")
            self.addButton( button )         

        # draw extra
        for i in range(0, len( self.extra ) ):
            position_y = positon_y_start + (total_rows * button_margin_y)
            position_x = positon_x_start + (i * button_margin_x)

            button = CalculatorButton((position_x, position_y), (button_width, button_height), (220, 220, 220), (255, 0, 0), self.addSymbolToEquation, f"{self.extra[i]}", f"{self.extra[i]}")
            self.addButton( button )    

        total_rows += 1

        # calculate button
        # correct position inline to be topleft
        position_y = positon_y_start + (total_rows * button_margin_y)
        position_x = positon_x_start
        calculate = Button((position_x + ( button_width/2), position_y + ( button_height/2)), (button_width, button_height), (40, 180, 40), (40, 220, 40), self.calculate, "=",)
        self.addButton( calculate )

        # clear button
        # correct position inline to be topleft
        position_y = positon_y_start + (total_rows * button_margin_y)
        position_x = positon_x_start + (1 * button_margin_x)
        clear = Button((position_x + ( button_width/2), position_y + ( button_height/2)), (button_width, button_height), (220, 220, 220), (255, 0, 0), self.clearEquation, "CE",)
        self.addButton( clear )

        return

    def _drawCalculator( self ) -> None:
        """Update method every frame"""

        # draw equation
        pygame.draw.rect( self.m_renderer.m_screen, (255, 255, 255), pygame.Rect(25, 75, 350, 60))


        text = self.m_renderer.m_font_48.render( f"{self.equation}", False, (0, 0, 0))
        self.m_renderer.m_screen.blit( text, ( 150, 85 ) )

        return

    #
    # koppelcode
    #
    def geKoppelCode( self ) -> None:
        self.koppel_code_text = self.m_context.m_koppelcode.get_random_code( 4 )

    def _initKoppelcode( self ) -> None:
        """This gets executed when tab opens"""

        button = Button((200, 150), (225, 50), (220, 220, 220), (255, 0, 0), self.geKoppelCode, 'Genereer koppel code')
        self.addButton( button )
        return

    def _drawKoppelcode( self ) -> None:
        """Update method every frame"""
        text = self.m_renderer.m_font_48.render( f"{self.koppel_code_text}", False, (255, 255, 255))
        
        self.m_renderer.m_screen.blit( text, ( 150, 50 ) )


        return

    #
    # notes
    #

    def _initNotes( self ) -> None:
        """This gets executed when tab opens"""
        self.note = TextInput(25, 75, 350, self.m_renderer.m_font_48)
        self.addTextInput( self.note )

        button = Button((200, 200), (100, 50), (220, 220, 220), (255, 0, 0), self.saveNote, 'Opslaan')
        self.addButton( button )
        

    def _drawNotes( self ) -> None:
        """Update method every frame"""

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
    
    #
    # guilders euros conversion
    #
    def guilders_to_euros( self ) -> None:
        print( f"{self.equation} euro’s to guilders: {self.m_context.m_calculator.euros_guilders_conversion(self.equation)}")
        return
    
    def euros_to_guilders( self ) -> None:
        print( f"{self.equation} guilders to euro’s: {self.m_context.m_calculator.euros_guilders_conversion(self.equation, False)}")
        return

    def _initGuldens( self ) -> None:
        """This gets executed when tab opens"""

        self.equation = ""

        positon_x_start = 40
        positon_y_start = 200

        row = 0
        column = 0
        total_columns = 0
        total_rows = 0

        # draw numeric buttons
        for i in range(1,10):
            position_y = positon_y_start + (row * 60)
            position_x = positon_x_start + (column * 50)

            button = CalculatorButton((position_x, position_y), (40, 50), (220, 220, 220), (255, 0, 0), self.addToEquation, f"{i}", f"{i}")
            self.addButton( button )

            column += 1
            
            if i % 3 == 0:
                row += 1
                total_columns += 1
                total_rows += 1
                column = 0
        
        # # draw modifiers
        # button_letters = ["+", "-", "x", ":"]
        # modifiers = ["+", "-", "*", "/"]
        # for i in range(0, len( modifiers ) ):
        #     position_y = positon_y_start + (i * 60)
        #     position_x = positon_x_start + (total_columns * 50)
        #     button = CalculatorButton((position_x, position_y), (40, 50), (220, 220, 220), (255, 0, 0), self.addToEquation, f"{modifiers[i]}", f"{button_letters[i]}")
        #     self.addButton( button )         

        # draw extra
        extra = ["0", ".", ","]
        for i in range(0, len( extra ) ):
            position_y = positon_y_start + (total_rows * 60)
            position_x = positon_x_start + (i * 50)

            button = CalculatorButton((position_x, position_y), (40, 50), (220, 220, 220), (255, 0, 0), self.addToEquation, f"{extra[i]}", f"{extra[i]}")
            self.addButton( button )    

        total_rows += 1

        # guilders button
        position_y = positon_y_start + (total_rows * 60)
        position_x = positon_x_start
        guilders = Button((position_x, position_y), (70, 50), (220, 220, 220), (255, 0, 0), self.euros_to_guilders, "€ → ƒ",)
        self.addButton( guilders )

        # euros button
        position_y = positon_y_start + (total_rows * 60)
        position_x = positon_x_start + (1 * 80)
        euros = Button((position_x, position_y), (70, 50), (220, 220, 220), (255, 0, 0), self.guilders_to_euros, "ƒ → €",)
        self.addButton( euros )

        return

    def _drawGuildersConversion( self ) -> None:
        """Update method every frame"""

        # draw equation
        text = self.m_renderer.m_font_48.render( f"{self.equation}", False, (255, 255, 255))
        self.m_renderer.m_screen.blit( text, ( 150, 50 ) )

        return

    def callGuiMethod( self ) -> None:
	    print(".")