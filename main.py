import sys

import pygame
from pygame.sprite import Group
from pygame.time import Clock

# app core modules
from modules.app.settings import Settings
from modules.app.renderer import Renderer

# app specific modules
from modules.gui.gui import Gui
from modules.calculator import Calculator
from modules.notes import Notes
from modules.koppelcode import KoppelCode

class Application:
    """Base class for this application"""
    # app core modules
    m_settings      : Settings
    m_clock         : Clock
    m_renderer      : Renderer

    # app specific modules
    m_gui           : Gui
    m_notes         : Notes
    m_koppelcode    : KoppelCode
    m_calculator    : Calculator

    def __init__( self ) -> None:
        """Init game"""
        pygame.init()
        self.m_settings = Settings()
        self.m_clock = pygame.time.Clock()

        # initialize renderer
        self.m_renderer = Renderer( self )
        self.m_renderer.create_screen_instance()

        self._init_modules()

    def _init_modules( self ) -> None:
        """Initialize specific application modules"""
        self.m_gui = Gui( self )
        self.m_notes = Notes( self )
        self.m_koppelcode = KoppelCode( self )
        self.m_calculator = Calculator( self )

    def _update_screen( self ) -> None:
        """Handle screen clearing, drawing and uploading to swapchain"""
        self.m_renderer.clearFramebuffer()

        # draw/blit begin
        self.m_gui.draw()
        # draw/blit end

        self.m_renderer.endFrame()

    def _handle_key_down( self, event ) -> None:
        """Handle key-down"""
        return

    def _handle_events( self ) -> None:
        """Handle input and state events"""
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_key_down( event )

        self.m_gui.event_handler( event_list )

    def run( self ) -> None:
        """main loop"""
        while True:
            self._handle_events()
            self._update_screen()

            # update modules
            self.m_notes.update()
            self.m_koppelcode.update()
            self.m_calculator.update()

            self.m_clock.tick( self.m_settings.m_target_fps )

# ??
if __name__ == '__main__':
    app = Application()
    app.m_renderer.updateWindow( resolution=( 400, 600 ) )
    app.m_settings.setBackgroundIcon( 'assets/app/icon.png' );
    app.m_settings.setClearColor( (152.0, 199.0, 243.0) )

    app.m_gui.openTab( app.m_gui.TAB_CALCULATOR )
    app.run()
    