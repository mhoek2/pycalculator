import sys

import pygame
from pygame.sprite import Group
from pygame.time import Clock

from modules.app.settings import Settings
from modules.app.renderer import Renderer

class Calculator:
    """Base class for the app"""
    m_settings      : Settings
    m_clock         : Clock
    m_renderer      : Renderer

    def __init__( self ) -> None:
        """Init game"""
        pygame.init()
        self.m_settings = Settings()
        self.m_clock = pygame.time.Clock()

        # renderer
        self.m_renderer = Renderer( self )
        self.m_renderer.create_screen_instance()

    def _update_screen( self ) -> None:
        self.m_renderer.clearFramebuffer()

        # draw/blit begin
        # draw/blit end

        self.m_renderer.endFrame()

    def _handle_events( self ) -> None:
        """Handle input and state events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run( self ) -> None:
        """main loop"""
        while True:
            self._handle_events()
            self._update_screen()
            self.m_clock.tick( self.m_settings.m_target_fps )

# ??
if __name__ == '__main__':
    app = Calculator()
    app.m_renderer.updateWindow( resolution=( 400, 600 ) )
    app.m_settings.setBackgroundIcon( 'assets/app/icon.png' );
    app.m_settings.setClearColor( (0.0, 0.0, 0.0) )

    app.run()