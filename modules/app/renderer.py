from ast import Tuple
import sys
import pygame

from pygame.font import Font

class Renderer:
    """Handle rendering related math and methods"""
    m_screen            : pygame.Surface
    m_font_16           : Font
    m_font_48           : Font

    def __init__( self, context ) -> None:
        self.m_context = context
        self.m_settings = context.m_settings

        pygame.font.init()
        self.m_font_16 = pygame.font.SysFont('Calibri', 16)
        self.m_font_48 = pygame.font.SysFont('Calibri', 48)

    def create_screen_instance( self ) -> None:
        """Set up screen instance, resolution, title etc"""
        self.updateWindow( self.m_settings.m_resolution )
        pygame.display.set_caption( self.m_settings.m_window_title )

    def updateWindow( self, resolution : Tuple = False, flags : int = False ):
        if resolution:
            self.m_settings.m_resolution = resolution;
        
        if flags:
            self.m_settings.m_window_flags = flags;

        self.m_screen = pygame.display.set_mode( 
           self.m_settings.m_resolution, 
           self.m_settings.m_window_flags
        )

    def clearFramebuffer( self ) -> None:
        """Clear framebuffer for current swapchain image"""
        self.m_screen.fill( self.m_settings.m_clear_color )

    def endFrame( self ) -> None:
        """Upload the current framebuffer to the swapchain image"""
        pygame.display.flip()